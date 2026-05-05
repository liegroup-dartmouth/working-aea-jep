$(document).ready(function () {

    // ── Sidebar toggle for mobile ──────────────────────────────────────────
    $('#sidebar-toggle-btn').on('click', function () {
        $('.sidebar-content').toggleClass('active');
    });

    // ── Folder expand/collapse ─────────────────────────────────────────────
    $('.folder-title').on('click', function () {
        var $items = $(this).next('.sidebar-folder-items');
        var $icon  = $(this).find('.folder-icon');
        $items.toggleClass('collapsed');
        if ($items.hasClass('collapsed')) {
            $icon.removeClass('fa-minus-square').addClass('fa-plus-square');
        } else {
            $icon.removeClass('fa-plus-square').addClass('fa-minus-square');
        }
    });

    // ── Expand all ────────────────────────────────────────────────────────
    $('.sidebar-expand-all').on('click', function () {
        $('.sidebar-folder-items').removeClass('collapsed');
        $('.folder-icon').removeClass('fa-plus-square').addClass('fa-minus-square');
    });

    // ── Collapse all ──────────────────────────────────────────────────────
    $('.sidebar-collapse-all').on('click', function () {
        $('.sidebar-folder-items').addClass('collapsed');
        $('.folder-icon').removeClass('fa-minus-square').addClass('fa-plus-square');
    });


    // ══════════════════════════════════════════════════════════════════════
    //  SEARCH
    // ══════════════════════════════════════════════════════════════════════

    var searchIndex  = null;   // Lunr index (built lazily)
    var searchDocs   = [];     // flat document store
    var indexBuilding = false; // guard against concurrent builds
    var pendingQuery  = null;  // query waiting for the index to finish

    /**
     * Escape a string for safe use inside a RegExp.
     */
    function escapeRegex(str) {
        return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    /**
     * Build a text snippet (~200 chars) centred on the first occurrence of
     * any query word, with all query words wrapped in <mark>.
     */
    function makeSnippet(text, query) {
        if (!text) return '';
        var words  = query.toLowerCase().split(/\s+/).filter(Boolean);
        var lower  = text.toLowerCase();
        var idx    = -1;

        for (var i = 0; i < words.length; i++) {
            idx = lower.indexOf(words[i]);
            if (idx !== -1) break;
        }

        var start   = Math.max(0, idx === -1 ? 0 : idx - 80);
        var end     = Math.min(text.length, start + 220);
        var snippet = (start > 0 ? '…' : '') +
                      text.slice(start, end) +
                      (end < text.length ? '…' : '');

        // Highlight every matching word
        words.forEach(function (word) {
            var re = new RegExp('(' + escapeRegex(word) + ')', 'gi');
            snippet = snippet.replace(re, '<mark>$1</mark>');
        });
        return snippet;
    }

    /**
     * Render search results into the #search-results panel.
     */
    function showResults(query) {
        var $panel = $('#search-results');
        $panel.empty();

        if (!query || query.length < 2) {
            $panel.hide();
            return;
        }

        var results = [];
        try {
            // Wildcard / fuzzy: try exact phrase first, fall back to fuzzy
            results = searchIndex.search(query);
            if (results.length === 0) {
                results = searchIndex.search(query.split(/\s+/).map(function (t) {
                    return t + '~1';
                }).join(' '));
            }
        } catch (e) {
            // Lunr throws on invalid query tokens; try word-by-word
            try {
                results = searchIndex.search(query.split(/\s+/).join(' '));
            } catch (e2) { results = []; }
        }

        if (results.length === 0) {
            $panel.html('<div class="search-no-results">No results found.</div>').show();
            return;
        }

        var shown = 0;
        results.slice(0, 10).forEach(function (result) {
            var doc = searchDocs[result.ref];
            if (!doc) return;
            shown++;

            var snippet = makeSnippet(doc.snippet || doc.content, query);

            var $item    = $('<div class="search-result-item" role="option">');
            var $title   = $('<a class="search-result-title">').attr('href', doc.url).text(doc.title);
            var $meta    = doc.authors
                             ? $('<span class="search-result-authors">').text(doc.authors)
                             : null;
            var $snippet = $('<p class="search-result-snippet">').html(snippet);

            $item.append($title);
            if ($meta) $item.append($meta);
            $item.append($snippet);
            $panel.append($item);
        });

        if (shown === 0) {
            $panel.html('<div class="search-no-results">No results found.</div>');
        }
        $panel.show();
    }

    /**
     * Fetch both data sources, build the Lunr index, then run any pending
     * query.
     */
    function buildIndex() {
        if (searchIndex || indexBuilding) return;
        indexBuilding = true;

        var base = (typeof siteBaseurl !== 'undefined') ? siteBaseurl : '';

        Promise.all([
            fetch(base + '/search.json').then(function (r) { return r.json(); }),
            fetch(base + '/papers/article-index.json').then(function (r) { return r.json(); })
        ]).then(function (data) {
            var pages       = data[0];
            var articleData = data[1];

            searchDocs = {};   // keyed by string id for O(1) lookup

            // ── Jekyll pages (index, about, etc.) ──────────────────────────
            (pages || []).forEach(function (page) {
                if (!page.title || !page.url) return;
                var id = 'page-' + page.id;
                searchDocs[id] = {
                    id:      id,
                    title:   page.title,
                    url:     page.url,
                    content: page.content || '',
                    snippet: (page.content || '').slice(0, 500),
                    type:    'page'
                };
            });

            // ── Papers from article-index.json ─────────────────────────────
            var articles = (articleData && articleData.articles) ? articleData.articles : [];
            articles.forEach(function (article, i) {
                if (!article.paper_url) return;   // skip journal-level front matter

                var authorsStr  = (article.authors || []).join(', ');
                var figTitles   = (article.figures_titles || []).join(' ');
                var searchText  = [
                    article.title    || '',
                    authorsStr,
                    article.miniabstract || '',
                    figTitles
                ].join(' ');

                var id = 'paper-' + i;
                searchDocs[id] = {
                    id:      id,
                    title:   article.title || '(untitled)',
                    url:     article.paper_url,
                    authors: authorsStr,
                    content: searchText,
                    snippet: article.miniabstract || searchText,
                    type:    'paper'
                };
            });

            // ── Build Lunr index ───────────────────────────────────────────
            searchIndex = lunr(function () {
                this.ref('id');
                this.field('title',   { boost: 10 });
                this.field('authors', { boost: 6  });
                this.field('content');

                Object.values(searchDocs).forEach(function (doc) {
                    this.add(doc);
                }, this);
            });

            indexBuilding = false;

            // Run any query that came in while we were building
            if (pendingQuery !== null) {
                showResults(pendingQuery);
                pendingQuery = null;
            }
        }).catch(function (err) {
            console.error('[search] Index build failed:', err);
            indexBuilding = false;
        });
    }

    // ── Wire up the search input ───────────────────────────────────────────
    var searchTimer = null;

    $('#search-input').on('input', function () {
        clearTimeout(searchTimer);
        var query = $(this).val().trim();

        if (!query || query.length < 2) {
            $('#search-results').hide().empty();
            return;
        }

        searchTimer = setTimeout(function () {
            if (!searchIndex) {
                pendingQuery = query;
                buildIndex();          // result shown via pendingQuery when ready
            } else {
                showResults(query);
            }
        }, 200);   // 200 ms debounce
    });

    // Close the results panel when the user clicks outside
    $(document).on('click', function (e) {
        if (!$(e.target).closest('#search-form, #search-results').length) {
            $('#search-results').hide();
        }
    });

    // Close on Escape
    $('#search-input').on('keydown', function (e) {
        if (e.key === 'Escape') {
            $('#search-results').hide();
            $(this).val('');
        }
    });

    // Kick off index build as soon as the page is idle
    if (window.requestIdleCallback) {
        requestIdleCallback(buildIndex);
    } else {
        setTimeout(buildIndex, 1000);
    }
});

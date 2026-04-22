$(document).ready(function () {
    // Sidebar toggle for mobile
    $('#sidebar-toggle-btn').on('click', function () {
        $('.sidebar-content').toggleClass('active');
    });

    // Folder expand/collapse
    $('.folder-title').on('click', function () {
        var $items = $(this).next('.sidebar-folder-items');
        var $icon = $(this).find('.folder-icon');
        $items.toggleClass('collapsed');
        if ($items.hasClass('collapsed')) {
            $icon.removeClass('fa-minus-square').addClass('fa-plus-square');
        } else {
            $icon.removeClass('fa-plus-square').addClass('fa-minus-square');
        }
    });

    // Expand all
    $('.sidebar-expand-all').on('click', function () {
        $('.sidebar-folder-items').removeClass('collapsed');
        $('.folder-icon').removeClass('fa-plus-square').addClass('fa-minus-square');
    });

    // Collapse all
    $('.sidebar-collapse-all').on('click', function () {
        $('.sidebar-folder-items').addClass('collapsed');
        $('.folder-icon').removeClass('fa-minus-square').addClass('fa-plus-square');
    });
});
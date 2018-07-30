
function CustomFileBrowser(field_name, url, type, win) {

    var cmsURL = '/admin/filebrowser/browse/?pop=2';
    cmsURL = cmsURL + '&type=' + type;

    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 980,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'no',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no'
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

tinyMCE.init({

    // see
    // http://wiki.moxiecode.com/index.php/TinyMCE:Configuration

    // Init
    mode: 'textareas',
    theme: 'advanced',

    // General
    //accessibility_warnings: false,
    browsers: 'gecko,msie,safari,opera',
    dialog_type: 'window',
    editor_deselector: 'mceNoEditor',
    keep_styles: false,
    language: 'en',
    object_resizing: false,
    media_strict: true,

    // Callbackss
    file_browser_callback: CustomFileBrowser,

    // Layout
    width: 1000,
    height: 800,
    indentation: '10px',

    // Cleanup
    cleanup: true,
    cleanup_on_startup: true,
    element_format: 'xhtml',
    fix_list_elements: true,
    fix_table_elements: true,
    fix_nesting: true,
    forced_root_block : 'p',

    // URL
    relative_urls: false,
    document_base_url: '127.0.0.1:8000',
    remove_script_host: true,

    // Content CSS
    // content_css : "css/example.css",

    // Plugins
    plugins: 'advimage,advlink,fullscreen,paste,media,searchreplace, template',

    // Theme Advanced
    theme_advanced_toolbar_location: 'top',
    theme_advanced_toolbar_align: 'left',
    theme_advanced_statusbar_location: 'bottom',
    theme_advanced_buttons1: 'formatselect,styleselect,|,bold,italic,underline,|,bullist,numlist,blockquote,|,undo,redo,|,link,unlink,|,image,|,fullscreen,|,grappelli_adv',
    theme_advanced_buttons2: 'search,|,pasteword,template,media,charmap,|,code,|,table,cleanup,grappelli_documentstructure',
    theme_advanced_buttons3: '',
    theme_advanced_path: false,
    theme_advanced_blockformats: 'p,h2,h3,h4,pre',
    theme_advanced_resizing: true,
    theme_advanced_resize_horizontal: false,
    theme_advanced_resizing_use_cookie: true,
    theme_advanced_styles: 'Image Left=img_left;Image Right=img_right;Image Block=img_block',

    // Style formats
    // see http://wiki.moxiecode.com/index.php/TinyMCE:Configuration/style_formats
    style_formats : [
        {title : 'Paragraph Small', block : 'p', classes: 'p_small'},
        {title : 'Paragraph ImageCaption', block : 'p', classes: 'p_caption'},
        {title : 'Clearfix', block : 'p', classes: 'clearfix'},
        {title : 'Code', block : 'p', classes: 'code'}
    ],

    // Templates
    // see http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/template
    // please note that you need to add the URLs (src) to your url-patterns
    // with django.views.generic.simple.direct_to_template
    template_templates : [
        {
            title : '2 Columns',
            src : '/path/to/your/template/',
            description : '2 Columns.'
        },
        {
            title : '4 Columns',
            src : '/path/to/your/template/',
            description : '4 Columns.'
        }
    ],

    // Adv
    advlink_styles: 'Internal Link=internal;External Link=external',
    advimage_update_dimensions_onchange: true,
});


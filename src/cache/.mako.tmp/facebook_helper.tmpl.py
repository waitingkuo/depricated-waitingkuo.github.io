# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394425251.790503
_enable_loop = True
_template_filename = u'/Users/willy/.virtualenvs/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/facebook_helper.tmpl'
_template_uri = u'facebook_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 62
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<div id="fb-root"></div>\n<script>\n  window.fbAsyncInit = function() {\n    // init the FB JS SDK\n    FB.init({\n      appId      : \'')
        # SOURCE LINE 8
        __M_writer(unicode(comment_system_id))
        __M_writer(u'\',\n      status     : true,\n      xfbml      : true\n    });\n\n  };\n\n  // Load the SDK asynchronously\n  (function(d, s, id){\n     var js, fjs = d.getElementsByTagName(s)[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(s); js.id = id;\n     js.src = "//connect.facebook.net/en_US/all.js";\n     fjs.parentNode.insertBefore(js, fjs);\n   }(document, \'script\', \'facebook-jssdk\'));\n</script>\n\n<div class="fb-comments" data-href="')
        # SOURCE LINE 25
        __M_writer(unicode(url))
        __M_writer(u'" data-width="470"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n<span class="fb-comments-count" data-url="')
        # SOURCE LINE 29
        __M_writer(unicode(link))
        __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n<div id="fb-root"></div>\n<script>\n    // thank lxml for this\n    $(\'.fb-comments-count\').each(function(i, obj) {\n        var url = obj.attributes[\'data-url\'].value;\n        // change here if you dislike the default way of displaying\n        // this\n        obj.innerHTML = \'<fb:comments-count href="\' + url + \'"></fb:comments-count> comments\';\n    });\n\n  window.fbAsyncInit = function() {\n    // init the FB JS SDK\n    FB.init({\n      appId      : \'')
        # SOURCE LINE 46
        __M_writer(unicode(comment_system_id))
        __M_writer(u'\',\n      status     : true,\n      xfbml      : true\n    });\n\n  };\n\n  // Load the SDK asynchronously\n  (function(d, s, id){\n     var js, fjs = d.getElementsByTagName(s)[0];\n     if (d.getElementById(id)) {return;}\n     js = d.createElement(s); js.id = id;\n     js.src = "//connect.facebook.net/en_US/all.js";\n     fjs.parentNode.insertBefore(js, fjs);\n   }(document, \'script\', \'facebook-jssdk\'));\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



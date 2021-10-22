import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging
from ckan.lib.plugins import DefaultTranslation
from ckan.common import request

log = logging.getLogger(__name__) 
def tags_and_counts():
    q_result = toolkit.get_action('package_search')(
        data_dict={'facet.field': '["tags"]'}
    )

    result = q_result[u'facets'][u'tags']

    return result

def all_groups():
    groups = toolkit.get_action('group_list')(
        data_dict={'all_fields': True})    
  
    return groups

def recent_datasets(count=None):
    datadict = {'sort' : 'relevance asc, metadata_modified desc, last_modified desc'}

    if count:
        datadict['rows'] = count

    datasets = toolkit.get_action('package_search')(
        data_dict=datadict
    )

    return datasets['results']

def cookies_accepted():
    value = request.cookies.get('cookie_consent')
    return value == 'true'

def cookies_asked():
    value = request.cookies.get('cookie_consent')
    return value is not None

class Custom_ThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.ITranslation)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'custom_theme')

        

    def get_helpers(self):
        return {
            'custom_theme_tags_and_counts': tags_and_counts,
            'custom_theme_groups': all_groups,
            'custom_theme_recent_datasets': recent_datasets,
            'custom_theme_cookies_check': cookies_accepted,
            'custom_theme_cookies_asked': cookies_asked
        }

    

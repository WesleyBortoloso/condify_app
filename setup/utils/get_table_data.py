from supabase import create_client 
from django.conf import settings
import logging

def get_table_data(table_name):
    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    logger = logging.getLogger(__name__)


    response = supabase.table(table_name).select('*').execute()
        
    if response:
        data = response.data
        logger.error(f" {data}")
        return data
    else:
        return []

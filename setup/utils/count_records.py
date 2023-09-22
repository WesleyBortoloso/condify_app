from supabase import create_client 
from django.conf import settings
import logging

def count_records_in_tables():
    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
    logger = logging.getLogger(__name__)

    tabelas = ["residents_resident", "apartments_apartment", "notifications_notification", "garages_garage", "wallet_wallet"]

    counts = {}
    
    for tabela in tabelas:
        response, count = supabase.table(tabela).select('*', count='exact').execute()
        
        if count:
            counter = count[1]
            counts[tabela] = counter
            logger.error(f"Contagem de registros em {tabela}, {response}, {counter}")
        else:
            data = response.json()
            counts[tabela] = data[0]["count"]
            logger.info(f"Falha ao contar registros em {tabela}: {response}")

    return counts
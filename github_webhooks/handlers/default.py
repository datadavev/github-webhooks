import logging
from typing import Optional

from github_webhooks.schemas import WebhookHeaders


async def handle_default(event: str, headers: WebhookHeaders, payload: bytes) -> Optional[str]:
    logging.debug('Default handler for <%s> event, headers: %s, payload: %s', event, headers, payload)
    return 'OK'

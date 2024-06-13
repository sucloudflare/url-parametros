from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

url = 'https://www.lp.nemu.com.br/?utm_source=fb&utm_campaign=adset01|123&utm_medium=campanha01|1234&utm_content=ad|1234'

partes = urlparse(url)
parametros = parse_qs(partes.query)

base = 'https://suasaudemental.com.br/'
nova = urlparse(base)

query_string = urlencode(parametros, doseq=True)
nova_url = urlunparse((
    nova.scheme,
    nova.netloc,
    nova.path,
    nova.params,
    query_string,
    nova.fragment
))

print('Nova URL: 'nova_url)


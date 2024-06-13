<h1>Manipulação de URLs em Python</h1> 
<p>Este script Python demonstra como manipular URLs utilizando a biblioteca <code>urllib.parse</code>. Ele realiza as seguintes operações:</p>
<ul>
    <li><strong>Análise da URL de Entrada:</strong> A URL inicial é analisada usando <code>urlparse</code>, que a divide em seus componentes principais como esquema (scheme), netloc, path, query string, etc.</li>
<li><strong>Extração de Parâmetros da Query String:</strong> Os parâmetros da query string são extraídos usando <code>parse_qs</code>, que os converte em um dicionário.</li>

<li><strong>Montagem de uma Nova URL:</strong> Uma nova URL base é definida (<code>https://suasaudemental.com.br/</code>). Utilizando <code>urlparse</code>, seus componentes são analisados.</li>

<li><strong>Codificação de Parâmetros:</strong> Os parâmetros extraídos da query string são codificados de volta em uma string de query string usando <code>urlencode</code>.</li>

<li><strong>Montagem da Nova URL Completa:</strong> Utilizando <code>urlunparse</code>, os componentes da nova URL são combinados com a query string codificada para formar uma nova URL completa.</li>
</ul>
<h2>Como Usar</h2>
<p>Para executar o script:</p>
<ol>
    <li>Certifique-se de ter Python instalado em seu ambiente.</li>
<li>Copie o código Python fornecido (<code>url_parametros.py</code>) para um arquivo local.</li>

<li>Execute o script usando um interpretador Python:</li>

<pre><code class="language-bash">python url_parametros.py</code></pre>

<li>O resultado será a impressão da nova URL formada com base na URL base e nos parâmetros da URL de entrada.</li>
</ol>
<h2>Exemplo</h2>
<p>Suponha que a URL de entrada seja:</p>
<pre><code class="language-plaintext">https://www.lp.nemu.com.br/?utm_source=fb&amp;utm_campaign=adset01</code></pre>
<p>A saída do script será uma nova URL com base na URL base definida (<code>https://suasaudemental.com.br/</code>), mantendo os parâmetros da URL original:</p>
<pre><code class="language-plaintext">https://suasaudemental.com.br/?utm_source=fb&amp;utm_campaign=adset01</code></pre>
<h2>Referências</h2>
<ul>
  <li><a href="https://docs.python.org/3/library/urllib.parse.html">Documentação <code>urllib.parse</code> - Python</a></li>
</ul>
<p>Este README fornece uma visão geral de como o script manipula URLs usando a biblioteca padrão <code>urllib.parse</code> do Python. Personalize conforme necessário para integrar com seu projeto ou aplicação específica.</p>

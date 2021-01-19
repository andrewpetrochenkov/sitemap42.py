<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/sitemap42.svg?maxAge=3600)](https://pypi.org/project/sitemap42/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/sitemap42.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/sitemap42.py/actions)

### Installation
```bash
$ [sudo] pip install sitemap42
```

#### Examples
```python
from sitemap42 import Sitemap

sitemap = Sitemap()
sitemap.append('https://domain.com/page1', )
sitemap.append('https://domain.com/page2', changefreq='daily', priority=0.5, lastmod=datetime.now())

sitemap.tostring()
sitemap.write('sitemap.xml')
```

```python
from sitemap42 import Sitemapindex

sitemapindex = Sitemap()
sitemapindex.append('https://domain.com/sitemap1.xml')
sitemapindex.append('https://domain.com/sitemap2.xml', lastmod=datetime.now())
```

#### Links
+   [Sitemaps XML format](https://www.sitemaps.org/protocol.html)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>

__all__ = ['Sitemap', 'Siteindex']

import io
import xml.dom.minidom
import xml.etree.cElementTree as etree
import xml.etree.ElementTree as ElementTree

XMLNS = "http://www.sitemaps.org/schemas/sitemap/0.9"
CHANGEFREQ = ['always', 'hourly', 'daily', 'weekly',
              'monthly', 'yearly', 'never']


class Root:
    root_tag = None
    element_tag = None

    def __init__(self, items=None):
        if not items:
            items = []
        self.items = items

    def append(self, loc, **kwargs):
        kwargs['loc'] = loc
        self.items.append(kwargs)

    def _to_etree(self):
        root = etree.Element(self.root_tag)
        root.attrib['xmlns'] = XMLNS
        for item in self.items:
            doc = etree.SubElement(root, self.element_tag)
            etree.SubElement(doc, 'loc').text = item['loc']
            if 'lastmod' in item:
                lastmod = item['lastmod'].strftime('%Y-%m-%d')
                etree.SubElement(doc, 'lastmod').text = lastmod
            if 'changefreq' in item:
                changefreq = item['changefreq']
                if changefreq not in CHANGEFREQ:
                    raise ValueError('invalid changefreq: %s' % changefreq)
                etree.SubElement(doc, 'changefreq').text = changefreq
            if 'priority' in item:
                etree.SubElement(
                    doc, 'priority').text = '%0.1f' % item['priority']
        tree = etree.ElementTree(root)
        return tree

    def tostring(self):
        tree = self._to_etree()
        with io.BytesIO() as f:
            tree.write(f, encoding='utf-8', xml_declaration=False)
            string = f.getvalue().decode('utf-8')
            string = string.replace('<?xml version="1.0" ?>',
                                    '<?xml version="1.0" encoding="UTF-8"?>')
            dom = xml.dom.minidom.parseString(string)
            return dom.toprettyxml(encoding="utf-8").decode("utf-8")

    def write(self, filename):
        tree = self._to_etree()
        tree.write(filename, encoding='utf-8', xml_declaration=True)

    def __str__(self):
        return self.tostring()


class Sitemap(Root):
    root_tag = 'urlset'
    element_tag = 'url'


class Sitemapindex(Root):
    root_tag = 'sitemapindex'
    element_tag = 'sitemap'

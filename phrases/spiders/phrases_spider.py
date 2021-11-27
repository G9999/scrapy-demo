"""
    phrases/spides/phrases_spiders.py
    ~~~~~~~~~~~~~~

    Spider for phrases project.
"""

import scrapy


class PhrasesSpider(scrapy.Spider):
    """Spider for collecting phrases."""

    name = "phrases"  # the spider name. Used to call run (`scrapy crawl phrases`).

    def start_requests(self):
        """Start the requests with the initial urls."""

        # iterate over all the urls
        for page in range(1, 407):
            url = f'https://www.ofrases.com/tema/vida/{page}'
            yield scrapy.Request(url=url, callback=self.parse)
        for page in range(1, 227):
            url = f'https://www.ofrases.com/tema/amor/{page}'
            yield scrapy.Request(url=url, callback=self.parse)
        for page in range(1, 165):
            url = f'https://www.ofrases.com/tema/hombres/{page}'
            yield scrapy.Request(url=url, callback=self.parse)
        for page in range(1, 49):
            url = f'https://www.ofrases.com/tema/mujeres/{page}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):  # pylint: disable=no-self-use
        """Parse the phrases alongtside their authors from the response."""

        # grab all the blockquote elements
        blocks = response.xpath("//blockquote")

        # open the text tile
        with open('phrases.txt', 'a') as phrases_file:
            for block  in blocks:
                # extract the phase and the author from each blockquote
                phrase = block.xpath('a/text()').get()
                author = block.xpath('small/cite/a/text()').get()

                # format the result
                full_quote = f"{phrase}\n- {author}"
                # save to file
                phrases_file.write(f'{full_quote}\n')

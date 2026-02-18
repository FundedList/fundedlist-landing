module.exports = function(eleventyConfig) {
  // Pass through all existing static files
  eleventyConfig.addPassthroughCopy("img");
  eleventyConfig.addPassthroughCopy("favicon.ico");
  eleventyConfig.addPassthroughCopy("favicon-16x16.png");
  eleventyConfig.addPassthroughCopy("favicon-32x32.png");
  eleventyConfig.addPassthroughCopy("apple-touch-icon.png");
  eleventyConfig.addPassthroughCopy("_headers");
  eleventyConfig.addPassthroughCopy("admin");
  eleventyConfig.addPassthroughCopy("robots.txt");

  // Blog collection sorted by date descending
  eleventyConfig.addCollection("posts", function(collectionApi) {
    return collectionApi.getFilteredByGlob("blog/posts/*.md").sort((a, b) => b.date - a.date);
  });

  // Date formatting filter
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return new Date(dateObj).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  });

  // Excerpt filter — first 160 chars of content
  eleventyConfig.addFilter("excerpt", (content) => {
    if (!content) return '';
    const text = content.replace(/<[^>]+>/g, '').replace(/\n/g, ' ').trim();
    return text.length > 160 ? text.substring(0, 157) + '...' : text;
  });

  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      data: "_data"
    },
    passthroughFileCopy: true,
    htmlTemplateEngine: false,
    markdownTemplateEngine: "njk"
  };
};

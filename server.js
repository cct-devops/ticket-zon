
module.exports = (opts) => {
  const fastify = require('fastify')(opts)
  
  fastify.get('/products', async (request, reply) => {
    const searchTerm = request.query['search']
    const products = require('./products.json')
    
    let filteredProducts = []
    if (searchTerm) {
      for(product of products) {
        if (product.name.includes(searchTerm)){
          filteredProducts.push(product)
        }
      }
    } else {
      filteredProducts = products
    }

    return filteredProducts
  })

  return fastify
}

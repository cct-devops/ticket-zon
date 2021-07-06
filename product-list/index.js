const fastify = require('fastify')({
  logger: true
})

fastify.get('/products', async(request, reply) => {
  const searchTerm = request.query['search']
  const products = require('./products.json')
  
  if (!searchTerm) return products
  
  const filteredProducts = []
  for(product of products) {
    if (product.name.includes(searchTerm)){
      filteredProducts.push(product)
    }
  }
  return filteredProducts
})

const start = async () => {
  try {
    await fastify.listen(3000)
  } catch (err) {
    fastify.log.error(err)
    process.exit(1)
  }
}
start()

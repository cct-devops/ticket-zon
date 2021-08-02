
module.exports = (opts) => {
  const fastify = require('fastify')(opts)
  const axios = require('axios')
  const jwt = require('jsonwebtoken')

  const validTokens = {}

  fastify.get('/products', async (request, reply) => {
    const auth = request.headers['authorization']
    if (!auth) {
      return reply.code(401).send({ status: 'Unauthorized' })
    }
    const token = auth.split(' ')[1]

    // TODO: Check timestamp
    console.log('token was not found')
    try{
      await axios.get(`http://auth-service/jwt-verify?token=${token}`)
      validTokens[token] = 1
    } catch(e) {
      console.log(e)
      return reply.code(401).send({ status: 'Unauthorized' })
    }

    const searchTerm = request.query['search']
    const products = require('./products.json')
    let filteredProducts = []
    if (searchTerm) {
      for (product of products) {
        if (product.name.includes(searchTerm)) {
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

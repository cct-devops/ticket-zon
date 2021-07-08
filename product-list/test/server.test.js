

var assert = require('assert')
const server = require('../server')

const expect = require('chai').expect

describe('Products list', function() {
    it('should return 200 when invoked', async function() {
      app = server({logger: false})
      const response = await app.inject({
        method: 'GET',
        url: '/products'
      })

      expect(response.statusCode).to.equal(200)
    })

    it('should return 1 product when searching "cream"', async function() {
      app = server({logger: false})
      const response = await app.inject({
        method: 'GET',
        url: '/products?search=cream'
      })
      expect(response.statusCode).to.equal(200)
      expect(JSON.parse(response.payload).length).to.equal(1)
    })

    
    it('should return 0 products when searching "bananas"', async function() {
      app = server({logger: false})
      const response = await app.inject({
        method: 'GET',
        url: '/products?search=bananas'
      })
      expect(response.statusCode).to.equal(200)
      expect(JSON.parse(response.payload).length).to.equal(0)
    })
})

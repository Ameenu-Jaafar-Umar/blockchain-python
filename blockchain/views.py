from django.http import JsonResponse
from .blockchain import Blockchain

blockchain = Blockchain()

def mine_block(request):
    proof = 12345  # Simplified proof-of-work for demo
    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return JsonResponse(response)

def get_chain(request):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return JsonResponse(response)

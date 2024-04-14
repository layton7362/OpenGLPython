from __future__ import annotations
# import glm
import typing
import Core

class AssetManager:
    asset: map[Core.Resource, Core.Resource] = {}
    
    @staticmethod
    def exist(res: Core.Resource):
        return res in AssetManager.asset
    
    @staticmethod
    def get(res: Core.Resource):
        if AssetManager.exist(res):
            return AssetManager.asset[res]
        return None

    @staticmethod
    def add(res: Core.Resource):
        if not AssetManager.exist(res):
            AssetManager.asset[res] = res

    @staticmethod
    def remove(res: Core.Resource):
        if AssetManager.exist(res):
            map_data = AssetManager.get(res)
            del AssetManager.asset[res]
            return map_data
        return None
            
if __name__ == "__main__":

    mystr = Core.Base_Material()
    res = AssetManager.exist(mystr)
    assert(not res)
    AssetManager.add(mystr)
    res = AssetManager.exist(mystr)
    assert(res)
    data = AssetManager.remove(mystr)
    res = AssetManager.exist(mystr)
    assert(not res)

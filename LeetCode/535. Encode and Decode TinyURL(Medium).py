class Codec:
    def __init__(self):
        self.url2idx={}
        self.idx2url={}
        self.base="http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if self.url2idx.get(longUrl,-1)!=-1:
            pass
        else:
            L=len(self.url2idx)
            self.url2idx[longUrl]=str(L)
            self.idx2url[str(L)]=longUrl
        
        return self.base+self.url2idx[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        idx=shortUrl.replace(self.base,"")
        return self.idx2url[idx]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

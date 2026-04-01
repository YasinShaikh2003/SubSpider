import aiohttp

async def crtsh(domain):

    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    results = set()

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                data = await resp.json()

                for entry in data:
                    names = entry["name_value"].split("\n")

                    for sub in names:
                        if domain in sub:
                            results.add(sub.strip())
        except:
            pass

    return results


async def hackertarget(domain):

    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    results = set()

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                text = await resp.text()

                for line in text.split("\n"):
                    if "," in line:
                        sub = line.split(",")[0]
                        results.add(sub.strip())
        except:
            pass

    return results
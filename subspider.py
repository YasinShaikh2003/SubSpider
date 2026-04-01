import argparse
import asyncio
from sources import crtsh, hackertarget
from dns_resolver import resolve_domains
from utils import banner, save_results

async def run(domain, output):

    banner()

    print(f"[+] Target Domain: {domain}")
    print("[+] Collecting subdomains...\n")

    results = set()

    crt_results = await crtsh(domain)
    ht_results = await hackertarget(domain)

    results.update(crt_results)
    results.update(ht_results)

    print(f"[+] Passive Subdomains Found: {len(results)}")

    print("\n[+] Resolving IP Addresses...\n")

    resolved = resolve_domains(results)

    for sub, ip in resolved:
        print(f"[+] {sub}  -->  {ip}")

    print(f"\n[+] Active Subdomains: {len(resolved)}")

    if output:
        save_results(resolved, output)
        print(f"[+] Results saved to {output}")


def main():

    parser = argparse.ArgumentParser(
        description="SubSpider - Passive Subdomain & IP Discovery Tool"
    )

    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("-o", "--output", help="Save results to file")

    args = parser.parse_args()

    asyncio.run(run(args.domain, args.output))


if __name__ == "__main__":
    main()
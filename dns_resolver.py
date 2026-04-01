import dns.resolver

def resolve_domains(domains):

    resolver = dns.resolver.Resolver()
    results = []

    for domain in domains:
        try:
            answers = resolver.resolve(domain, "A")

            for rdata in answers:
                ip = rdata.to_text()
                results.append((domain, ip))

        except:
            pass

    return results
import dns.resolver


def lookup(domain, record_type, nameserver="8.8.8.8"):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [nameserver]
    resolver.timeout = 3
    resolver.lifetime = 5

    try:
        answers = resolver.resolve(domain, record_type)

        return {
            "domain": domain,
            "record_type": record_type,
            "nameserver": nameserver,
            "results": [str(answer) for answer in answers],
            "status": "success",
        }

    except dns.resolver.NXDOMAIN:
        return {"status": "nxdomain", "domain": domain}

    except dns.resolver.NoAnswer:
        return {
            "status": "no_answer",
            "domain": domain,
            "record_type": record_type,
        }

    except dns.exception.Timeout:
        return {"status": "timeout", "domain": domain}

    except dns.exception.DNSException as error:
        return {
            "status": "error",
            "domain": domain,
            "error": str(error),
        }

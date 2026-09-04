from collections.abc import Iterable, Mapping


def plan(services: Iterable[Mapping[str, object]]) -> list[dict[str, object]]:
    """Create a deterministic deployment plan from service definitions."""
    result = []
    for service in services:
        name = str(service.get("name", "")).strip()
        image = str(service.get("image", "")).strip()
        replicas = service.get("replicas", 1)
        if not name or not image:
            raise ValueError("each service needs name and image")
        if isinstance(replicas, bool) or not isinstance(replicas, int) or replicas < 1:
            raise ValueError("replicas must be a positive integer")
        result.append({"name": name, "image": image, "replicas": replicas})
    return sorted(result, key=lambda item: str(item["name"]))

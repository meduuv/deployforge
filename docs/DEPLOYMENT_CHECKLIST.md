# Deployment Checklist

Use this checklist before promoting a deployment configuration.

- [ ] Validate configuration syntax.
- [ ] Confirm required environment variables exist without committing secrets.
- [ ] Pin or verify dependency versions where reproducibility matters.
- [ ] Run automated tests and health checks.
- [ ] Confirm the service binds to the intended interface and port.
- [ ] Review logs for startup errors.
- [ ] Verify rollback steps before a production rollout.
- [ ] Perform a post-deployment smoke test.

Keep production credentials outside source control and CI logs.
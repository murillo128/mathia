# MI-061 — Square-root TV is the sharp Hilbert snowflake boundary

**Evidence level:** exact metric synthesis from [AF-466](../../findings/AF-466-square-root-tv-is-exactly-hilbertian-at-the-cost-of-lipschitz-sensitivity.md) and [AF-467](../../findings/AF-467-tv-snowflakes-have-a-sharp-half-exponent-hilbert-threshold.md), read against the finite-upper-Lipschitz cube obstruction AF-464. The negative-type/Schoenberg ingredient is classical; the line-specific content is the exact boundary for the TV source metric and the sensitivity price paid when it is crossed.

For the probability simplex with the Arithmetic Fidelity convention `d_TV(mu,nu)=||mu-nu||_1`, the subgraph map

`Phi(mu)(a,t)=1_[0,mu(a)](t)`

satisfies exactly

`||Phi(mu)-Phi(nu)||_H^2 = d_TV(mu,nu)`.

Thus `(Delta(A),d_TV^(1/2))` is isometric to a Hilbert subset, with no support-complexity or arithmetic restriction. More generally, every power metric `d_TV^alpha` with `0<alpha<=1/2` is Hilbertian.

The endpoint is sharp. For every `alpha>1/2`, the paired-mixture `k`-cube from AF-464 gives, for any Hilbert-valued bi-Lipschitz representation with lower gain `kappa` and upper gain `L` in `d_TV^alpha`,

`kappa <= L k^(1/2-alpha)`.

Hence the distortion is at least `k^(alpha-1/2)`, and no complexity-independent Hilbert fidelity exists on the full infinite simplex for any power snowflake milder than the square root.

The escape therefore changes the metric rather than defeating the cube geometry. Relative to the original TV distance, the explicit square-root embedding keeps a uniform inverse bound because `d_TV<=2`, but its forward TV-Lipschitz modulus is infinite: infinitesimal TV changes are magnified like `sqrt(d_TV)`. A downstream theorem may use this repair only if it actually consumes the snowflaked geometry or can tolerate that singular forward sensitivity; it cannot silently inherit a two-sided TV-Lipschitz claim.

**Boundary.** This is a metric-category result, not a compression theorem. The subgraph embedding retains the full labelled law and may be infinite-dimensional. It does not show that finite-dimensional, compact, positive, spectral or arithmetic quotients preserve the repaired metric, and it does not prove that the physical arithmetic source is naturally measured by `sqrt(d_TV)`.
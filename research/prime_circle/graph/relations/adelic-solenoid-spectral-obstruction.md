---
id: RGR-PC-SOLENOID-001
type: research-graph-relation
scope: prime_circle
relation: adelic-solenoid-spectral-obstruction
derived: true
---

# Compatible-circle solenoid and the proper-scale obstruction

[[research/prime_circle/findings/PC-064-compatible-circle-refinement-is-the-adelic-solenoid|PC-064]] identifies the all-level compatible-circle inverse limit with the classical arithmetic solenoid. [[research/prime_circle/findings/PC-065-solenoid-leafwise-laplacian-has-dense-rational-square-spectrum|PC-065]] then shows that its canonical leafwise Laplacian has dense rational-square spectrum, noncompact resolvent, infinite heat trace, and no intrinsic spectral-zeta half-plane.

The next source-backed refinements close increasingly broad attempts to obtain a proper transverse or coupled scalar scale from that same carrier:

- [[research/prime_circle/findings/PC-066-transverse-profinite-symmetry-fixes-exact-order-projectors-not-rh-hamiltonian|PC-066]] shows that translation/unit symmetry fixes exact-order projectors but leaves their spectral scale arbitrary.
- [[research/prime_circle/findings/PC-067-compatible-inverse-square-chord-energy-resolves-order-but-not-rh-scale|PC-067]] derives the uniquely compatible inverse-square chord energy, but it still resolves exact order without fixing an RH scale.
- [[research/prime_circle/findings/PC-068-regular-commuting-leaf-fiber-calculus-cannot-be-compact|PC-068]] shows that regular commuting scalar leaf-fiber functional calculus cannot produce compact resolvent.
- [[research/prime_circle/findings/PC-069-exact-solenoid-dilation-covariance-forbids-compact-resolvent|PC-069]] rules out an ordinary compact-resolvent Hamiltonian with exact homogeneous solenoid-dilation covariance.
- [[research/prime_circle/findings/PC-070-additive-solenoid-dilation-covariance-also-forbids-compact-resolvent|PC-070]] closes the corresponding additive/cocycle covariance escape on the full representation and its natural mean-zero subspace.

The supported chain is therefore:

```text
compatible refinement
    -> classical arithmetic solenoid
    -> leaf spectrum is noncoercive/noncompact
    -> transverse symmetry fixes order, not scale
    -> compatible regular leaf/fiber scales remain nonproper
    -> exact scalar/additive dilation covariance is incompatible with compact resolvent
```

This is a scoped obstruction stack, not closure of every solenoidal or adelic construction. The current Prime-Circle synthesis explicitly leaves singular, noncommuting, one-sided, representation-changing, or otherwise intrinsically forced scales outside these no-go classes.
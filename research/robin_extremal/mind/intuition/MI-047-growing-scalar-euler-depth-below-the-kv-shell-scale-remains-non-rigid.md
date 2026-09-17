# MI-047 — Growing scalar Euler depth up to the KV shell scale remains non-rigid

**Evidence level:** exact constructive synthesis from RE-173, RE-178, RE-182, [RE-184](../../findings/RE-184-growing-euler-jet-depth-below-kv-shell-scale-remains-nonrigid.md), and [RE-185](../../findings/RE-185-chebyshev-shell-interpolation-removes-the-growing-jet-log-loss.md). The constant-fraction KV range is sufficient, not claimed sharp.

The failure of scalar Euler data is not confined to fixed dimension. Let

`V(p)=(log p)^(3/5)/(log log p)^(1/5)`.

RE-184 already constructed ordinary-prime-supported `{0,1,2}` controls matching every Euler boundary derivative through depth `K` when `K log(K+2)=o(V(p))`, while preserving every fixed Korobov--Vinogradov source envelope and an order-one transient Robin displacement. RE-185 shows that the `log K` loss was not source rigidity but a basis-conditioning artifact.

After normalizing the logarithmic repair shell and using a Chebyshev-type interpolation basis, the repair overhead becomes `exp(O(K))`. There is therefore an absolute `c_*>0` such that every

`1 <= K <= c_* V(p)`

can still be matched exactly by an ordinary-prime-supported `{0,1,2}` source with the same KV fidelity and transient Robin ambiguity. In particular every `K=o(V(p))` is admissible without choosing a small constant.

This sharpens the reusable mechanism: **scalar-family dimension becomes meaningful only after the interpolation geometry is conditioned optimally**. A growth barrier seen in raw monomials can be an artifact of coordinates rather than a source-capacity threshold. Here the honest source fibre absorbs a constant fraction of the full KV shell scale once the repair basis is adapted to that shell.

The live transition is therefore no longer the `K log K` regime. RE-178 places the raw higher-jet capacity scale much higher, at `K_cap(p) asymp log p/log log p`, while RE-185 proves non-rigidity through `K=Theta(V(p))`. Any scalar-jet rigidity theorem must either cross the KV shell scale by a genuine source obstruction or use joint/nonlocal placement information that shell interpolation cannot reproduce.

**Boundary.** RE-185 does not reach the RE-178 capacity scale or prove that `V(p)` is a sharp barrier. The repair still uses an infinite continuation and the declared `{0,1,2}` ordinary-prime source class; finite perturbations remain rigid under RE-172. The conclusion does not make the full Euler germ cheaply conditioned and does not address arbitrary growing separated-temperature panels.
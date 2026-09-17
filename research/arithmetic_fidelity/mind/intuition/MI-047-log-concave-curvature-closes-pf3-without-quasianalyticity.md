# MI-047 — Adjacent curvature mass is the exact smooth `PF_3` recognition variable

**Evidence level:** exact synthesis from [AF-385](../../findings/AF-385-sampled-solid-minor-hierarchy-certifies-continuum-fixed-order-total-nonnegativity.md), [AF-389](../../findings/AF-389-multiscale-solid-pf3-excludes-all-finite-order-boundary-contact.md), [AF-390](../../findings/AF-390-quasianalytic-curvature-closes-multiscale-pf3-recognition.md), [AF-391](../../findings/AF-391-log-concave-logarithmic-curvature-forces-order-three-total-nonnegativity.md), and [AF-392](../../findings/AF-392-adjacent-curvature-masses-exactly-characterize-smooth-order-three-fidelity.md).

For a positive `C^3` profile `f`, write

`q=-(log f)''`.

When `q>0`, AF-392 identifies the exact finite-window variable controlling continuum order-three total positivity. For adjacent gaps `a,b>0`, set

`A_a(t)=int_(t-a)^t q(s) ds`,

`B_(a,b)(t)=int_(t-a-b)^(t-a) q(s) ds`.

Then the translation kernel `K_f(x,y)=f(x-y)` is `TN_3` exactly when, for every `t,a,b`,

`A+B+B'/B-A'/A >= 0`.

Equivalently, after normalizing a three-column minor to the curve `(1,U(t),V(t))`, this inequality says that `V` is convex as a function of the strictly increasing coordinate `U`. Thus arbitrary order-three placements are controlled by a **comparison of two adjacent curvature masses and their logarithmic drift**, not by a pointwise curvature inequality alone.

AF-391 is now best understood as a strong sufficient cone inside this exact criterion. If `q` is log-concave, then `(log q)'` is nonincreasing, which forces the adjacent-window drift term to have the favorable sign and makes the AF-392 inequality automatic. But log-concavity is not necessary: AF-392 gives smooth oscillatory examples such as `q_epsilon(t)=1+epsilon cos t` that are not log-concave yet remain `TP_3` for sufficiently small `epsilon`.

The relation to the shrinking-mesh hierarchy is also exact. Letting `a,b -> 0` in the finite-window criterion gives

`(log q)'' <= 2q`,

the same local differential condition recovered in AF-388. Hence the shrinking local inequality is only the **infinitesimal shadow** of the continuum placement problem. The information missing from a local solid-minor limit is precisely the family of finite adjacent-window comparisons. Any source or category theorem that upgrades the multiscale certificate to full `TN_3` must somehow recover those comparisons, or imply them indirectly.

AF-389--AF-390 still control the boundary where `q` can vanish. Compatible shrinking lattices force every zero of `q` to be infinitely flat, and a flat-jet uniqueness theorem closes that residual fibre. AF-391 supplies a different closure route when the curvature shape itself is log-concave. AF-392 does not classify curvature zeros because its exact ratio criterion assumes `q>0`; a limiting version across flat zeros remains a separate boundary problem.

The reusable distinction is therefore sharper than “quasianalytic versus nonquasianalytic” or “log-concave versus non-log-concave.” In the strictly positive smooth region, `PF_3` is exactly a **finite-window curvature-transport condition**. Quasianalyticity and log-concavity are sufficient mechanisms that make the required global placement information follow from simpler source-class structure; neither is the definition of the surviving fibre.

**Boundary.** AF-392 makes no novelty claim relative to the classical `PF_3` literature and may be a smooth specialization of Weinberger's characterization. It also does not derive the adjacent-window inequality from arithmetic data, classify `q=0` boundary points, or produce an RH zero-selection theorem. The arithmetic-fidelity problem is to determine what retained source information can force the finite-window criterion, not merely its infinitesimal limit.
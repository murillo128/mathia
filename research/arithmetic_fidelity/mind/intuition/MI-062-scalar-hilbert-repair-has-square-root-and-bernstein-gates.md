# MI-062 — Smooth scalar Hilbert repair on TV is exactly a bounded Bernstein mixture

**Evidence level:** exact radial-kernel classification from [AF-468](../../findings/AF-468-any-scalar-hilbert-repair-must-amplify-tv-at-least-square-root.md), [AF-470](../../findings/AF-470-replicated-private-atoms-force-full-diameter-complete-alternation.md), and [AF-471](../../findings/AF-471-bounded-bernstein-signs-classify-smooth-radial-tv-hilbert-repairs.md). The negative-type and positive-definite kernel ingredients are classical; the line-specific content is their exact specialization to the full TV diameter of unrestricted finitely supported probability mixtures.

For a continuous radial squared-distance law `g:[0,2]->[0,infinity)` that is smooth on `(0,2)` and is required to be conditionally negative definite on every finite family of probability measures under total variation, AF-471 closes the necessity/sufficiency gap left by AF-470. The condition is exactly

`(-1)^(k-1) g^(k)(t) >= 0` for every `k>=1` and `0<t<2`,

equivalently

`g(t)=sum_(n>=1) a_n [1-(1-t/2)^n]`, with `a_n>=0` and `sum_n a_n=g(2)`.

Writing the overlap kernel as `S(mu,nu)=1-d_TV(mu,nu)/2`, every term `1-S^n` is a squared Hilbert distance after the tensor-power embedding. Thus the full smooth radial class is not merely constrained by complete alternation: it has an explicit positive-mixture realization.

The small-scale square-root gate remains load-bearing for the corresponding distance transform. AF-468 already shows that a complexity-independent bounded-distortion scalar Hilbert repair cannot stay locally Lipschitz-equivalent to TV: it must amplify the forced small scales at least at square-root order. AF-471 therefore closes the smooth exact radial branch rather than opening a smoother escape.

The compact TV diameter matters. These bounded-interval mixtures are a larger class than restrictions of global Bernstein functions on `[0,infinity)`; for example AF-471 gives a smooth polynomial member that satisfies the bounded interval sign hierarchy without being a global Bernstein function. The correct object is therefore the bounded overlap variable `S in [0,1]`, not an assumed global radial extension.

**Boundary.** The classification uses the breadth of the unrestricted mixture simplex over an infinite discrete alphabet and applies only to scalar radial exact Hilbertization. It does not show that a narrower physical arithmetic source realizes the private-atom tests, and it does not rule out non-radial source-forced structure. Any surviving route must therefore identify a genuine source restriction, retain non-radial/marked provenance through later quotients, or prove that the destination can consume the singularly changed metric without silently restoring the original TV fidelity requirement.
# MI-008 — A local mixed-response obstruction needs unbounded source moment or an uncontrolled residual map

**Evidence level:** proved operator boundaries; the factorization of the complete physical mixed response remains open.

For the fixed physical window `I=(-T,T)` and cutoff `kappa`, let `E_n` span the restrictions of `exp(2pi i k t/L_n)` with `|2pi k/L_n|<=kappa`, where `L_n -> infinity`, and put `V_n=E_n^perp`. [PF-292](../../findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor.md) proves that the constrained Dirichlet frequency floor `inf_{phi in V_n cap H_0^1, ||phi||_2=1}||phi'||_2` diverges. There are `R_n -> infinity` and `epsilon_n -> 0` such that, with `K_D=(-partial_t^2)_D^{1/2}`,

\[
\|P_{V_n}g_n\|_2\le\varepsilon_n\|g_n\|_2
+R_n^{-\sigma}\|K_D^\sigma g_n\|_2\quad(\sigma>0).
\]

Thus a uniformly bounded positive-Sobolev response cannot have a persistent high projection. No quantitative rate for `R_n` follows from this argument. The optimized mixed low/high correlation is the shorting deficit `delta=1-inf_h k[ell+h]/k[ell]` in the admissible high space ([PF-290](../../findings/PF-290-optimized-local-low-high-correlation-is-an-exact-high-band-shorting-deficit.md)); persistent positive deficits on separated coercive local witnesses obstruct compactness.

For the canonical fixed-axis component, [PF-296](../../findings/PF-296-weighted-source-row-moment-controls-canonical-fixed-axis-superpositions.md) supplies more than a fixed-row bound. If `y_(s,r)^(i)` is its normalized source column and `q_i=kappa_i^(1/2)c_i asymp kappa_i`, then uniformly for `s>0`, `0<r<=r_*`,

\[
\|U^*\sum_i a_i y_{s,r}^{(i)}\|_{H^{1/2}(\mathbb R)}
\le C_{r_*}\sum_i q_i|a_i|.
\]

The canonical tail already has bounded seam ratio. Therefore a complete response of the form `G_n=T_n Y_n(a_n)`, with the already-controlled positive-Sobolev transport `T_n` and `sup_n sum_i q_i|a_(n,i)|<infinity`, has vanishing local high projection and cannot sustain that deficit. Growing row count alone is not an escape: its weighted first moment must become unbounded along a subsequence, or the actual response must contain a residual mixed/reassembly operator outside this factorization.

This does not prove the factorization or bound its coefficients. Nor does absence of this local witness imply global compactness or weak trace class; the global heavy-range projection product and its singular-value counts remain separate objects.

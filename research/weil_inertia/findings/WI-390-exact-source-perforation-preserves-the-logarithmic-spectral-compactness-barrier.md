# WI-390 — Exact source perforation preserves the logarithmic spectral-compactness barrier

**Status:** `EXACT-DERIVED + CLASSICAL-INPUT + PRIME-POWER-SPARSITY + SOURCE-EXACT + DECISIVE-COERCIVITY-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-389 isolated the intrinsic recurrence-side compactness condition for fixed-width endpoint-adaptive profiles but left one explicit gate open: its logarithmic Fourier-tail hypothesis was only shown to kill the **unperforated** recurrence problem, because WI-387 had used a uniform `H^1` bound to transfer the exact prime-power source-slot cutoffs. That extra `H^1` gate is not genuine.

Fix `L>0`. For each integer `k`, let

\[
g_k\in C_c^\infty((-L/2,L/2);\mathbb R),
\qquad g_k(-s)=g_k(s),
\qquad \|g_k\|_2=1,
\tag{1}
\]

and write

\[
\widehat g_k(\xi)=\int_{\mathbb R}g_k(s)e^{i\xi s}\,ds,
\qquad
\ell(\xi)=\log(2+|\xi|).
\tag{2}
\]

Assume exactly the uniform logarithmic tail-integrability condition identified in WI-389,

\[
\boxed{
\delta(T):=
\sup_k\int_{|\xi|>T}\ell(\xi)|\widehat g_k(\xi)|^2\,d\xi
\longrightarrow0
\qquad(T\to\infty).
}
\tag{3}
\]

Let

\[
A_k=\log(k+1),
\qquad x_k=k+1,
\tag{4}
\]

and let `f_k^0` be the separated unperforated odd pair built from `g_k` as in WI-387. Let `f_k` be the corresponding **exact source-zero** odd trial obtained by imposing on the positive lobe the standard smooth Desogus prime-power source-slot cutoff and reflecting it with odd symmetry to the negative lobe. Then, under RH,

\[
\boxed{
\liminf_{k\to\infty}\mathcal W[f_k]=0.
}
\tag{5}
\]

More quantitatively, if `chi_k` is the centered positive-lobe cutoff, `eta_k=1-chi_k`, and

\[
r_k=\eta_k g_k
\tag{6}
\]

is the removed source piece, then for the whole-line screened difference form

\[
\widetilde D[v]
:=\frac12\iint_{\mathbb R^2}
 h(|s-t|)|v(s)-v(t)|^2\,ds\,dt,
\qquad
h(u)=\frac{e^{-u/2}}{1-e^{-2u}},
\tag{7}
\]

one has the uniform bound

\[
\boxed{
\|r_k\|_2^2+\widetilde D[r_k]
\ll_L
\delta(x_k^{1/4})+x_k^{-1/4}
\longrightarrow0.
}
\tag{8}
\]

Since `1+d(xi)` for the Fourier symbol of (7) is comparable to `log(2+|xi|)`, (8) is equivalent, up to fixed constants, to

\[
\boxed{
\int_{\mathbb R}\ell(\xi)|\widehat r_k(\xi)|^2\,d\xi\to0.
}
\tag{9}
\]

WI-389's fixed-exponential-type sampling estimate therefore gives

\[
\boxed{
\sum_\rho |\widehat r_k(\gamma)|^2\to0,
}
\tag{10}
\]

where `rho=beta+i gamma` runs over nontrivial zeta zeros with multiplicity. Under RH this makes the source-perforated and unperforated odd trials asymptotically identical in the Weil spectral norm. Combining (10) with WI-389/WI-387's coefficient-independent recurrence proves (5).

Thus the exact source slots do **not** move the scalar compactness threshold found in WI-389. In particular every uniformly bounded superlogarithmic moment

\[
\sup_k\int w(|\xi|)|\widehat g_k(\xi)|^2d\xi<\infty,
\qquad
\sup_{r\ge T}\frac{\log(2+r)}{w(r)}\to0,
\tag{11}
\]

already forces the source-exact zero floor; this includes `log^(1+delta)` for every `delta>0` and every uniform positive Sobolev regularity `H^s`, `s>0`. Conversely WI-388 still shows that a merely bounded logarithmic moment is insufficient to force compactness and that its escaping sideband can be placed on a diagonal sequence of exact source-zero endpoints. The log/superlog boundary therefore survives source exactness.

No established simple-critical-zero proportion changes, and no RH conclusion is claimed. This is a fixed-width coercivity barrier: any source-exact endpoint-adaptive fixed-width route that hopes to evade the recurrence obstruction must lose uniform logarithmic tail integrability itself, not merely lose `H^1` regularity.

## 1. The source cutoff has vanishing mass and capacity but only logarithmic pointwise cost

WI-384 sharpened the centered fixed-width prime-power slot count. For the smooth fixed-multiple enlargement used by the form-core cutoff, let `E_k` denote the support of `eta_k=1-chi_k`. Then

\[
\boxed{
\mu_k:=|E_k|
\ll_L \frac1{\sqrt{x_k}\log x_k}.
}
\tag{12}
\]

The screened cutoff-capacity estimate inherited from WI-377/WI-387 is

\[
\boxed{
\kappa_k:=\widetilde D[\eta_k]
=\widetilde D[\chi_k]
\ll_L x_k^{-1/2}.
}
\tag{13}
\]

Choose the standard smooth cutoff as a fixed profile of the distance to the union of enlarged slots. Every slot has width comparable to

\[
\varepsilon_k
=\log(1+1/k)\asymp x_k^{-1},
\tag{14}
\]

so

\[
0\le\eta_k\le1,
\qquad
\operatorname{Lip}(\eta_k)\ll x_k.
\tag{15}
\]

For later multiplication estimates define its pointwise screened jump density

\[
a_k(t)=
\int_{\mathbb R}
 h(|s-t|)|\eta_k(s)-\eta_k(t)|^2\,ds.
\tag{16}
\]

Using

\[
|\eta_k(s)-\eta_k(t)|
\ll \min\{1,x_k|s-t|\},
\tag{17}
\]

`h(u)\ll1/u` for `0<u<=1`, and the exponential tail of `h`, split the `u`-integral at `u=x_k^{-1}`. Uniformly in `t`,

\[
\boxed{
\|a_k\|_\infty\ll_L\log x_k.
}
\tag{18}
\]

On the other hand, by Fubini and (13),

\[
\boxed{
\int_{\mathbb R}a_k(t)\,dt
=2\widetilde D[\eta_k]
=2\kappa_k
\ll_Lx_k^{-1/2}.
}
\tag{19}
\]

Equations (18)-(19) identify the apparent difficulty below `H^1`: multiplication by the cutoff can cost a logarithm pointwise even though its total screened capacity vanishes. The Fourier-tail condition (3) is exactly strong enough to absorb that logarithm.

## 2. Split the profile below and above `R_k=x_k^(1/4)`

Let `P_R` denote the sharp Fourier projection to `[-R,R]`, and put

\[
R_k=x_k^{1/4},
\qquad
u_k=P_{R_k}g_k,
\qquad
e_k=g_k-\nu_k.
\tag{20}
\]

The whole-line form (7) has Fourier multiplier `d(xi)` from WI-373. The classical digamma representation gives

\[
0\le d(\xi)\ll\ell(\xi),
\qquad
\ell(\xi)\ll 1+d(\xi),
\tag{21}
\]

with constants independent of `k`. By (3), Plancherel, and `log R_k=(1/4)log x_k+O(1)`,

\[
\boxed{
\widetilde D[e_k]\ll_L\delta(R_k),
\qquad
\log x_k\,\|e_k\|_2^2\ll_L\delta(R_k).
}
\tag{22}
\]

The high-frequency part can now be multiplied by the source mask without losing control. From

\[
|\eta(s)e(s)-\eta(t)e(t)|^2
\le
2|e(s)-e(t)|^2
+2|e(t)|^2|\eta(s)-\eta(t)|^2,
\tag{23}
\]

(18) and (22) give

\[
\boxed{
\widetilde D[\eta_ke_k]
\le
2\widetilde D[e_k]
+\|a_k\|_\infty\|e_k\|_2^2
\ll_L\delta(R_k)	o0.
}
\tag{24}
\]

Also `||eta_k e_k||_2<=||e_k||_2=o(1)`. This is the key place where the logarithmic tail is used: the possible `log x_k` multiplier amplification is exactly cancelled by the `1/log R_k` gained when continuous Fourier energy above `R_k` is estimated from (3).

## 3. The low-frequency part sees only the vanishing source capacity

Because `nu_k` is bandlimited to `[-R_k,R_k]` and `||nu_k||_2<=1`, Bernstein/Cauchy--Schwarz estimates give

\[
\|\nu_k\|_\infty^2\ll R_k,
\qquad
\|\nu_k'\|_\infty^2\ll R_k^3.
\tag{25}
\]

For fixed `t`, define

\[
J_k(t)=
\int_{\mathbb R}
 h(|s-t|)|\nu_k(s)-\nu_k(t)|^2\,ds.
\tag{26}
\]

Using

\[
|\nu_k(s)-\nu_k(t)|^2
\ll
\min\{R_k,\ R_k^3|s-t|^2\},
\tag{27}
\]

split at `|s-t|=R_k^{-1}`. The `h(u)\ll1/u` singularity contributes `O(R_k)` below that scale and `O(R_k log R_k)` between `R_k^{-1}` and one; the exponential tail contributes `O(R_k)`. Hence

\[
\boxed{
\sup_t J_k(t)\ll R_k\log(2+R_k).
}
\tag{28}
\]

Apply the same product inequality as in (23), but now exploit that `eta_k` is supported on `E_k`. Equations (12), (13), (19), (25), and (28) give

\[
\begin{aligned}
\widetilde D[\eta_k\nu_k]
&\ll
\int_{E_k}J_k(t)\,dt
+\|\nu_k\|_\infty^2\int a_k(t)\,dt\\
&\ll
\mu_k R_k\log(2+R_k)+R_k\kappa_k\\
&\ll_L x_k^{-1/4}.
\end{aligned}
\tag{29}
\]

Likewise

\[
\boxed{
\|\eta_k\nu_k\|_2^2
\le
\mu_k\|\nu_k\|_\infty^2
\ll_L \frac{x_k^{-1/4}}{\log x_k}.
}
\tag{30}
\]

Since

\[
r_k=\eta_kg_k=\eta_k\nu_k+\eta_ke_k,
\tag{31}
\]

and `sqrt(D-tilde)` is a seminorm, (24), (29), and (30) prove (8). The fixed exponent `1/4` is only a convenient choice. Any cutoff frequency `R_k=x_k^a` with `0<a<1/2` works: the source capacity supplies `x_k^{-1/2}`, while logarithmic tail integrability absorbs the mask's `log x_k` pointwise cost.

## 4. The logarithmic form norm controls the zeta-sampled residual

The multiplier comparability (21) turns (8) into (9). WI-389 proved, by a fixed-support Schwartz reproducing kernel plus the Riemann--von Mangoldt unit-interval zero count, the unconditional sampling inequality

\[
\sum_\rho |\widehat v(\gamma)|^2
\ll_L
\int_{\mathbb R}\ell(\xi)|\widehat v(\xi)|^2\,d\xi
\tag{32}
\]

for every `v` supported in the same fixed interval. Applying (32) to `r_k` gives (10).

Now compare the actual source-zero trial with the unperforated even-profile pair. The positive lobe changes from `g_k` to `p_k=chi_k g_k=g_k-r_k`; the negative lobe is its reflected negative so that the full trial remains real and odd. At a critical-line zero, the Fourier transform of the full pair perturbation has magnitude at most `2|hat r_k(gamma)|`. Under RH the Weil form is the squared `l^2` norm of these sampled transforms, hence

\[
\mathcal W[f_k-f_k^0]
\le
4\sum_\gamma |\widehat r_k(\gamma)|^2
=o(1).
\tag{33}
\]

Therefore the Hilbert-space triangle inequality gives

\[
\left|
\sqrt{\mathcal W[f_k]}-
\sqrt{\mathcal W[f_k^0]}
\right|
\le
\sqrt{\mathcal W[f_k-f_k^0]}
=o(1).
\tag{34}
\]

WI-389 already showed from the same hypothesis (3) that the coefficient-independent Bohr/Kronecker recurrence of WI-387 gives

\[
\liminf_k\mathcal W[f_k^0]=0
\tag{35}
\]

under RH. Equations (34)-(35) prove (5). Moreover `||r_k||_2->0`, so each perforated lobe has norm tending to one and the full separated odd pair has norm tending to `sqrt(2)`. Thus (5) is also a zero Rayleigh-quotient statement; it is not caused by collapse of the test-vector norm.

## 5. What this closes, and the surviving escape

WI-389 explicitly left source transfer open because its proof only replaced the `H^1` hypothesis in the recurrence-side sampling step. Equations (12)-(34) close that exact gate. The same intrinsic compactness condition now controls both halves:

\[
\boxed{
\text{uniform log-weighted Fourier-tail integrability}
\Longrightarrow
\text{zeta-spectral tightness + negligible exact source perforation}.
}
\tag{36}
\]

Consequently a fixed-width endpoint-adaptive source-exact profile family cannot evade the RH-side recurrence barrier merely by leaving every bounded `H^1` class while retaining any superlogarithmic scalar moment. A surviving fixed-width route must instead exhibit genuine failure of (3): a nonvanishing amount of `log(2+|xi|)`-weighted Fourier energy must escape to arbitrarily high frequencies along some subsequence.

This is sharp at the scalar-moment level already isolated in WI-388/WI-389. A uniform bound on the total logarithmic moment does not imply the **uniform integrability** in (3); WI-388's `1/log R` sideband packet retains order-one zeta-sampled mass while paying only order-one logarithmic energy, and its diagonal source-zero realization shows that exact source slots do not remove that escape. Therefore this finding does not extend the no-go to the bare bounded-log-moment class.

For the canonical research objective this prunes, rather than solves, one possible defect-elimination route. Any fixed-width coercivity mechanism that could eventually detect every off-critical pair must now either exploit precisely such noncompact logarithmic spectral escape in a source-compatible way, control endpoint phases despite that escape, or change width/locality/domain/operator category. No claim is made against growing-width, multiscale, nonlocal, SDP, or domain-restricted constructions.

## Prior-art and novelty audit

The logarithmic Fourier scale itself is classical. Chen--Weth's logarithmic-Laplacian framework identifies the whole-line `2 log|xi|` high-frequency symbol underlying the screened form, and the logarithmic Sobolev-capacity literature studies related low-order capacity phenomena. Classical Plancherel--Polya/Bernstein theory supplies the bandlimited sup/derivative bounds and sampling context. These sources are already represented in `SOURCES.md` where load-bearing or directly contextual.

The zeta-specific sampling inequality (32) is the exact derived result of WI-389, based only on fixed exponential type and classical local zero counting. The source-hole measure and total screened capacity are exact derived consequences already established in WI-377/WI-384. A targeted external search around logarithmic-Laplacian capacity, perforated domains, Fourier-logarithmic spaces, and exponential-type sampling found no source stating the combined moving-prime-power perforation estimate (8), the balancing scale `R_k=x_k^(1/4)`, or the source-exact recurrence consequence (5). That negative search is not a priority claim.

The new deduction here is the frequency split that couples the two previously separate estimates. High frequencies absorb the cutoff's `O(log x_k)` pointwise multiplier cost using precisely the uniform logarithmic tail from WI-389; low frequencies pay only `R_k` times the `O(x_k^-1/2)` source capacity from WI-377/WI-384. Their compatible window `1<<R_k<<sqrt(x_k)` closes the source-transfer gap without any positive Sobolev bound.

## Evidence boundary

- **Classical / literature-backed:** Fourier representation and logarithmic high-frequency growth of the screened/digamma form; Bernstein estimates for bandlimited functions; Riemann--von Mangoldt local zero counts; Bohr/Kronecker finite-frequency recurrence; standard prime-power counting.
- **Persisted exact inputs:** WI-377/WI-384 source-hole measure and screened-capacity bounds; WI-389's fixed-support log-weighted zeta-sampling inequality and recurrence-side compactness criterion.
- **Exact deduction here:** the residual estimate (8), its log-Fourier consequence (9), the sampled residual convergence (10), and hence the source-exact zero-floor theorem (5) under RH.
- **Conditional:** the nonnegative Weil spectral norm and the final source-exact coercivity barrier are under RH, exactly as in WI-387/WI-389. The residual norm estimate (8) itself is harmonic analysis plus source geometry and does not assume RH.
- **Not claimed:** RH, an unconditional positive/negative Weil theorem, a new simple-critical-zero proportion, a non-RH adaptive-family dichotomy, or a barrier for families that fail logarithmic tail integrability.

## Consequence for the research program

The live fixed-width question left by WI-389 is resolved on its negative side: source exactness does not rescue any logarithmically compact adaptive profile family. The meaningful fixed-width frontier is now the genuinely noncompact regime exemplified by WI-388, where order-one logarithmic spectral resource escapes to increasing carrier frequencies. Further work on this architecture should therefore study whether endpoint phase, source geometry, or off-line signatures can control or exploit that noncompact regime; weakening `H^1` or replacing it by any superlogarithmic moment is no longer a live escape.
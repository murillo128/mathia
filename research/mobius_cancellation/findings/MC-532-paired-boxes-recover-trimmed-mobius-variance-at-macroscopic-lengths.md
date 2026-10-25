# MC-532 — Paired boxes recover trimmed Möbius variance at macroscopic lengths

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. No arithmetic variance ceiling is established.

## Claim and change of observation requirement

Let \(X\) be a positive integer, \(I_X=\{X,\ldots,2X-1\}\),
\(1\le H\le X/20\) an integer, and
\[
 L_1=H,\qquad L_2=K=\lfloor\sqrt2 H\rfloor,\qquad
 S_L(j)=M(j+L)-M(j).
\]
For each \(i=1,2\), independently choose a set \(E_i\subset I_X\),
\(B_i=|E_i|<X/2\), and one constant \(c_i\in\mathbb C\). Put
\[
 V_i=\sum_{j\in I_X\setminus E_i}|S_{L_i}(j)-c_i|^2.
\tag{1}
\]
If zeta has a zero \(\rho_0=\beta+i\gamma\), \(\beta>1/2\),
of multiplicity \(m\), then there exist \(C>0,X_0\) such that
\[
 \boxed{
 \frac{\sqrt{XV_1}+B_1^2}{H}
 +\frac{\sqrt{XV_2}+B_2^2}{K}
 \ge C X^\beta(\log X)^{m-1}}
\tag{2}
\]
for every integer \(X\ge X_0\), uniformly in the entire stated
range of \(H,E_i,c_i\). Constants depend on the selected zero and
the full hypothetical zero set, but not on these observation choices.
The masks need not coincide, and each center can be its own retained
empirical mean. No independence of the two window sums is assumed.

In particular, at \(H_X=\lfloor X/20\rfloor\), the following is
equivalent to RH: there exist an unbounded integer scale set
\(\mathcal X\) and families \(E_{i,X},c_{i,X}\), fixed before
the epsilon quantifier, such that, for every \(\varepsilon>0\),
uniformly for large \(X\in\mathcal X\), both channels satisfy
\[
 B_i\ll_\varepsilon X^{3/4+\varepsilon},\qquad
 V_i\ll_\varepsilon X^{1+\varepsilon}L_i.
\tag{3}
\]
Only an unbounded set is required; no scale density or spacing enters.

This resolves the local paired-box clue by combining three separately
audited ingredients: MC-528's reciprocal-pole test, the source-independent
two-box inverse in the explicitly granted PL-475 packet, and MC-531's
bounded-jump recovery. The substantive change from MC-531 is access to
macroscopic lengths at the price of **two** variance observations on
each block. Its single-length near-linear theorem remains unchanged.
Equation (3) is a strength test for unproved arithmetic input, not a
source of that input or a proof of RH.

## 1. A compatible test retains the full reciprocal principal part

Choose \(1/2<\sigma_0<\sigma_1<\beta\). MC-528, Sections 1–3,
constructs a compact smooth complex test \(\phi\) whose Mellin
transform \(\Phi\) satisfies
\[
 \Phi(1)=0,\qquad\Phi(\rho_0)=1,
\]
and vanishes to full multiplicity at every other zero with real part
greater than \(\sigma_0\). Its construction starts from a Gevrey
bump and applies a convergent derivative series. Choose that bump inside
\((\log(4/3),\log(5/3))\); multiplication by the exponential and
every derivative preserve this support. Thus
\[
 \phi\in C_c^\infty((4/3,5/3);\mathbb C),\qquad\int\phi=0.
\tag{4}
\]
The normalization remains nonzero: it is the product value at
\(\rho_0\) times the positive integral of the input bump.

The multiplicity-counted zero-density estimate, canonical-product
growth bound, and local division estimate of MC-528 apply without
change of hypotheses. In particular, after exact cancellation of nearby
zeros, the quotient has proved vertical decay. The justified contour
shift gives
\[
 T_\phi(X):=\sum_n\mu(n)\phi(n/X)
 =X^{\rho_0}Q_{m-1}(\log X)+O_\phi(X^{\sigma_1}),
\tag{5}
\]
where, writing \(1/\zeta(s)=\sum_{r=1}^m a_r(s-\rho_0)^{-r}
+\text{holomorphic}\),
\[
 Q_{m-1}(v)=\sum_{r=1}^m a_r
   \sum_{j=0}^{r-1}\frac{v^{r-1-j}\Phi^{(j)}(\rho_0)}{(r-1-j)!j!},
 \qquad [v^{m-1}]Q_{m-1}=\frac{a_m}{(m-1)!}\ne0.
\tag{6}
\]
Consequently \(|T_\phi(X)|\gg X^\beta(\log X)^{m-1}\) on
every sufficiently large block. The conjugate pole is cancelled; there
is no cosine zero along a selected scale sequence. A multiple pole
whose ordinary residue is zero still contributes the leading term in
(6). Neither a finite zero list nor mere meromorphic continuation
would justify (5).

## 2. Reconstruct the two-box inverse and its localization

Write \(\alpha=\sqrt2\), \(b_a=a^{-1}\mathbf1_{[0,a]}\),
and \(A_af=b_a*f\). The following reconstruction uses only the
source-independent part of
[[research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance|PL-475]],
Sections 1–3. It supplies compact finite-order distributions satisfying
\[
 b_1*T_1+b_\alpha*T_2=\delta_0,
\quad\operatorname{supp}T_1\subset[-1,1+\alpha],
\quad\operatorname{supp}T_2\subset[-1,1].
\tag{7}
\]

With Fourier convention \(\widehat b_a(\xi)=(1-e^{-ia\xi})/(ia\xi)\),
the quadratic-irrational bound \(\|\alpha n\|_{\mathbb Z}\gg1/|n|\)
implies
\[
 v_0=0,\qquad v_n=\widehat b_\alpha(2\pi n)^{-1}=O(n^2)
 \quad(n\ne0).
\]
Indeed, rationalizing \(|\sqrt2|n|-k|\) for the nearest integer
\(k\) uses the nonzero integer \(|2n^2-k^2|\ge1\).
The \(v_n\) define a periodic distribution \(V\); four derivatives
of a periodic test make its Fourier pairing absolutely summable.
Choose \(w\in C_c^\infty((-1,1))\) with
\(\sum_{j\in\mathbb Z}w(u+j)=1\), and set \(T_2=wV\).
Periodizing the test \(we^{-2\pi inu}\) proves
\(\widehat T_2(2\pi n)=v_n\), including zero.

Put \(D=\delta_0-b_\alpha*T_2\). Its support lies in
\([-1,1+\alpha]\), and its nonzero integral-frequency Fourier
samples vanish. The periodization of \(D'\) is therefore zero at
every frequency. With \(\tau_jF(u)=F(u-j)\), set
\[
 T_1=\sum_{j\ge0}\tau_jD'.
\]
This is locally finite. It vanishes to the left of \(-1\); to the
right of \(1+\alpha\) it equals the full, zero periodization,
since negative-index translates have vanished there. Thus it has the
support in (7) and finite order. Telescoping gives
\((I-\tau_1)T_1=D'\). Since \(b_1'=\delta_0-\delta_1\),
\((b_1*T_1-D)'=0\). The difference is a compactly supported
constant distribution, hence zero. This proves (7), including its
zero-frequency condition. In particular the masses of \(T_1,T_2\)
are respectively 1 and 0.

For a compact distribution define dilation by
\(\langle T_h,\psi\rangle=\langle T,\psi(h\,\cdot)\rangle\).
It preserves convolution and mass. Define
\[
 f_{1,h}=T_{1,h}*\phi,\qquad f_{2,h}=T_{2,h}*\phi.
\]
Dilating (7) and convolving with (4) gives exactly
\[
 A_hf_{1,h}+A_{\alpha h}f_{2,h}=\phi.
\tag{8}
\]
For \(0<h\le1/20\), both tests have integral zero and support in
\[
 J=[4/3-1/20,\,5/3+(1+\alpha)/20]\Subset(1,2).
\]
Finite distributional order \(M_i\) gives, for each fixed \(\ell\),
\[
 \|f_{i,h}^{(\ell)}\|_\infty
 \le C_i\sum_{r=0}^{M_i}h^r\|\phi^{(\ell+r)}\|_\infty
 \le C_{\phi,\ell}.
\tag{9}
\]
Apply the distribution to \(v\mapsto\phi^{(\ell)}(u-hv)\)
with a fixed cutoff near its support; every derivative of the latter
factor supplies \(h\). The common support also bounds the L2 norms.
This is a finite derivative cost on smooth targets, not bounded
inversion on arbitrary L2 data.

## 3. Rounding and two exact centered pairings

Let \(h=H/X\), \(k=K/X\); then \(|k-\alpha h|<X^{-1}\).
The identity \(A_af(u)=\int_0^1f(u-at)dt\) implies
\[
 \|A_af-A_bf\|_\infty\le\tfrac12|a-b|\|f'\|_\infty.
\]
Equations (8)–(9) therefore give
\[
 \|A_hf_{1,h}+A_kf_{2,h}-\phi\|_\infty\ll_\phi X^{-1}.
\tag{10}
\]
The error is supported in one fixed compact subset of \((0,3)\).
There are \(O(X)\) integers in its dilation, so \(|\mu(n)|\le1\)
charges only \(O_\phi(1)\) when (10) is summed against Möbius.

For each channel put
\[
 \mathcal L_i=\frac1{L_i}\int_X^{2X}
    (M(y+L_i)-M(y)-c_i)f_{i,h}(y/X)\,dy.
\]
Zero integral removes the arbitrary center exactly. Finite interchange
of the coefficient sum and integral yields
\[
 \mathcal L_i=\sum_n\mu(n)(A_{L_i/X}f_{i,h})(n/X).
\tag{11}
\]
The coefficient of \(\mu(n)\) is the test integral over
\([n-L_i,n]\), divided by \(L_i\), with the test extended by
zero. Thus endpoint-crossing windows are included without an extra
truncation. Combining (5), (10), and (11), uniformly in \(H\),
\[
 |\mathcal L_1+\mathcal L_2|
 =|T_\phi(X)+O_\phi(1)|
 \gg X^\beta(\log X)^{m-1}.
\tag{12}
\]

For integer \(L\), the window sum is constant on \([j,j+1)\),
and \(|S_L(j+1)-S_L(j)|\le2\). The discrete lemma of MC-531
then gives, separately for each mask and center,
\[
 \sum_{j\in I_X}|S_{L_i}(j)-c_i|
 \le2\sqrt{XV_i}+4B_i^2.
\tag{13}
\]
For clarity, when \(B\ge1\), an interval of \(2B+1\) indices
containing any omitted index has at least \(B+1\) retained indices
within distance \(2B\). Averaging the jump bound and applying
Cauchy–Schwarz bounds that omitted value by
\(\sqrt{V/(B+1)}+4B\). Summing omitted values and the retained
absolute mass proves (13); \(B=0\) is Cauchy–Schwarz alone.
Subtracting a constant preserves the jump bound, even for complex
centers. No fitted function of the start is allowed.

Now (9), (11), and (13) imply
\[
 |\mathcal L_i|\ll_\phi
       \frac{\sqrt{XV_i}+B_i^2}{L_i}.
\tag{14}
\]
The triangle inequality in (12) proves (2). The complete analytic tests
are never multiplied by the retained-set indicators. Separate masks
are paid for in the bounds, so they do not damage the cancellation of
unwanted poles or the two mean-zero conditions.

## 4. Quantifiers in the macroscopic criterion

For \(H=\lfloor X/20\rfloor\), both lengths are comparable to
\(X\). Under (3), the left side of (2) is
\[
 O_\varepsilon\bigl(X^{1/2+\varepsilon/2}
                       +X^{1/2+2\varepsilon}\bigr).
\tag{15}
\]
If \(\beta>1/2\), choose
\(0<\varepsilon<\min\{1/4,(\beta-1/2)/2\}\).
Equation (15) is \(o(X^\beta)\), contradicting (2) along the
unbounded set. Functional-equation symmetry then gives RH. The same
small epsilon ensures \(B_i<X/2\) eventually, so this auxiliary
condition is automatic from (3).

Conversely, under RH, MC-520 proves the complete uncentered bound
\(\sum_{j\in I_X}|S_L(j)|^2\ll_\varepsilon X^{1+\varepsilon}L\)
uniformly for integer \(1\le L\le X\). Take all large integer
scales, empty masks, and centers zero. This proves (3) simultaneously
for both lengths. Empirical centers only reduce the energies.

The families of scales, masks, and centers in (3) are chosen before
epsilon varies; the theorem asserts this precise quantified criterion.
Neither a bound at just one favorable member of the pair nor bounds
on unrelated scale sets provide (15). With empty masks, squaring (2)
also gives the consistency check
\(V_1/H^2+V_2/K^2\gg X^{2\beta-1}(\log X)^{2m-2}\).

## Prior art, controls, and evidence boundary

[Casey–Walnut (1994)](https://doi.org/10.1137/1036140) and
[Casey's 1996 report, Section 2.1, Theorems 2.3–2.4](https://api.drum.lib.umd.edu/server/api/core/bitstreams/fff4ad58-33f1-4d4f-b92d-1117c53a9efc/content)
(MC-S83) establish the classical compact-distribution Bezout framework;
the report explicitly treats box lengths with square-root-of-prime
ratio. [Pensky–Sapatinas (2011)](https://doi.org/10.1214/11-EJS597)
(MC-S84) studies Diophantine boxcar channels in a periodic statistical
model. Neither multichannel inversion nor its small-divisor requirement
is new here. The support and dilation argument above supplies the
specific localized smooth tests used against Möbius.

The variance/zero-location connection is also classical: MC-S67–MC-S73
support MC-520 and MC-528, and Zaccagnini's Selberg-integral discussion
(MC-S72) is adjacent prime-counting context. The almost-all cancellation
baseline of [Matomäki–Radziwiłł](https://doi.org/10.4007/annals.2016.183.3.6)
(MC-S1) is not a square-root-scale retained-energy estimate with the
quantitative deletion budget (3). A qualitative exceptional density
does not supply that budget. No external priority claim follows from
the literature comparison. The local derived result is precisely the
macroscopic, paired, trimmed certificate (2).

- **Rational and small-divisor controls.** An exact inverse (7) is
  impossible at rational ratio \(p/q\), whose multipliers share a
  zero at \(2\pi q\). At a Liouville ratio, the forced samples
  \(\widehat T_2(2\pi n)=\widehat b_\alpha(2\pi n)^{-1}\)
  grow faster than every polynomial along a subsequence, contradicting
  the real-axis growth bound for compact distributions. Irrationality
  without quantitative approximation control is insufficient.
- **Rounded rational pairs.** No exact inverse is asserted for
  \((H,K)\). Equation (10) retains its explicit error. When \(H=K=1\),
  the two channels may coincide; the approximate recovery still holds
  and its coefficient error is still \(O(1)\). No independence or
  division by \(K-H\) occurs.
- **Arithmetic scope.** The inverse and recovery lemma apply to generic
  bounded coefficients. Only MC-528's reciprocal-zeta formula supplies
  the pole obstruction for Möbius. An all-plus coefficient sequence has
  constant integer-window sums and fails those pole-test hypotheses.
  Generalized-prime or random multiplicative models inherit no such
  formula from deconvolution alone.
- **Deletion scope.** Whole integer starts are removed; a measurable
  mask splitting unit cells requires another argument. The exponent
  \(3/4\) is sufficient, not proved optimal for this signed test.
  MC-531's two-tent control proves sharpness only for generic absolute
  mass recovery, not optimality for Möbius or for phase-sensitive tests.
- **Non-effectivity and zero boundary.** The test depends on the full
  hypothetical zero set; there is no zero-uniform norm or onset, no
  effective finite-zero certificate, and no conclusion at
  \(\beta=1/2\) or about simplicity. The full multiplicity in (6)
  must not be replaced by the ordinary residue alone.

As an auxiliary indexing check, exact rational arithmetic verified the
two complete identities (11), zero-sum cell weights, and (13) in 160
paired bounded-coefficient cases with separate masks and centers.
These included coincident lengths and windows crossing the block end;
the test primitives were compact piecewise polynomials. This checks
normalization and discrete bookkeeping, not the distributional inverse,
analytic continuation, or actual zero location. The analytic derivation
is the evidence; no Lean check or independent adversarial approval is
asserted.

The inverse is established classical infrastructure and the finite
recovery lemma is elementary. Their composition does not create a new
formalization pressure test. The remaining substantive research task is
an independently justified joint arithmetic bound for the retained
energies and omitted counts on the same scales.

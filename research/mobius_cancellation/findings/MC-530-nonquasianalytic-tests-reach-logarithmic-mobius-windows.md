# MC-530 — Nonquasianalytic tests reach logarithmic Möbius windows

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. The new admissible window range comes from classical
compact smoothness and finite inversion. No arithmetic variance ceiling
is proved.

## Claim and mathematical delta

For real \(X\ge2\) and integer \(H\ge1\), define
\[
S_{X,H}(y)=M(y+H)-M(y),\qquad
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,
\]
\[
V_\mu(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2dy.
\]
If \(\rho_0=\beta+i\gamma\) is a zeta zero with
\(\beta>1/2\) and multiplicity \(m\), then for every fixed
\(r>1\) there are \(c>0,X_0\) such that
\[
\boxed{V_\mu(X,H)\ge cH^2X^{2\beta-1}(\log X)^{2m-2}}
\tag{1}
\]
for every real \(X\ge X_0\) and every integer
\[
1\le H\le\frac{X}{\log X(\log\log X)^r}.
\tag{2}
\]
Constants depend on \(r,\rho_0\) and the full hypothetical zero
set. There is no simplicity, rightmost-zero, spacing or reciprocal
residue-size assumption.

[MC-529](MC-529-single-near-linear-centered-variance-law-is-equivalent-to-rh.md)
proved the same floor through \(X/(\log X)^B\), each fixed
\(B>1\). Range (2) is strictly larger than each such range.
The new step verifies a stronger derivative class through the entire
multiplicity-aware annihilator, logarithmic composition and growing
finite box inverse. A Fourier envelope by itself would not justify
those operations. The construction resolves the local logarithmic-window
clue without supplying independent Möbius cancellation.

## 1. A compact derivative class preserved by the annihilator

Fix \(1<\kappa<r\), and put
\[
\ell_n=\log(e+n),\qquad W_n=n!\ell_n^{\kappa n},\qquad W_0=1.
\tag{3}
\]
There is a nonnegative nonzero \(\eta\in C_c^\infty((0,\log2))\)
with \(\|\eta^{(n)}\|_\infty\le CA^nW_n\).
Here is an explicit classical convolution construction, including the
derivative bound needed below. Take normalized interval densities of
widths \(a_0>0\) and
\(a_j=d/[j\ell_j^\kappa]\), \(j\ge1\).
Their widths have finite sum because \(\kappa>1\).
Scale and translate their infinite convolution into \((0,\log2)\).
It has mass one. Differentiate the factors indexed \(1,\ldots,n\)
in the distributional sense, leaving the zeroth factor undifferentiated.
Their total variations are \(2/a_j\), so
\[
\|\eta^{(n)}\|_\infty
 \le a_0^{-1}\prod_{j=1}^n\frac2{a_j}
 \le a_0^{-1}(2/d)^n n!\ell_n^{\kappa n}.
\tag{4}
\]
For each \(n\), the remaining interval factors give a continuous
convolution density, so these distributional derivatives are continuous.
The absolutely summable widths give a compactly supported probability
limit; this proves smoothness as well as the bound. This is the standard
[[research/prior_art/incremental/PA-nonquasianalytic-infinite-convolution-cutoff|iterated-convolution construction]], anchored in MC-S81.

The order-uniform inequality
\[
W_{j+n}\le D_\kappa^{j+n}W_jW_n,
\qquad D_\kappa=2^{1+\kappa},
\tag{5}
\]
is useful. For positive \(j,n\), concavity of \(\log(e+x)\)
gives \(\ell_j\ge j\ell_{j+n}/(j+n)\) and the corresponding
bound for \(n\). Hence
\[
\frac{\ell_{j+n}^{j+n}}{\ell_j^j\ell_n^n}
 \le\frac{(j+n)^{j+n}}{j^jn^n}\le2^{j+n}.
\]
Combine this with \((j+n)!\le2^{j+n}j!n!\). Zero indices
are immediate. Multiplication by a fixed exponential also preserves
a bound \(CA^nW_n\), by Leibniz's formula and monotonicity of \(W_n\).

Fix \(1/2<\sigma_0<\sigma_1<\beta\).
[MC-528](MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md),
Sections 1–2, supplies the multiplicity-counted density exponent
\(0<a<1\), the convergent product
\[
P(s)=(s-1)\prod_{\substack{\Re\rho>\sigma_0\\\rho\ne\rho_0}}
 (1-s/\rho)^{m_\rho}=\sum_{j\ge0}p_js^j,
\qquad |p_j|\le CB^j/(j!)^{1/a}.
\tag{6}
\]
All copies of the selected zero are omitted and its conjugate is retained.
Let \(g(t)=e^{-\rho_0t}\eta(t)\), and set
\[
k(t)=\sum_{j\ge0}p_j(-1)^jg^{(j)}(t),\qquad
D=P(\rho_0)\int\eta\ne0,\qquad \phi(u)=D^{-1}k(\log u).
\tag{7}
\]
For every \(n\), (5) yields
\[
\|k^{(n)}\|_\infty
 \le C(AD_\kappa)^nW_n
 \sum_{j\ge0}(ABD_\kappa)^j
       \frac{\ell_j^{\kappa j}}{(j!)^{1/a-1}}
 \le C' A_1^nW_n.
\tag{8}
\]
The series converges: its \(j\)-th root is at most a constant
times \((\log(e+j))^\kappa/j^{1/a-1}\), which tends to zero.
Its bound is independent of \(n\). Thus (7) converges in every
smooth norm, retains the common compact support, and preserves (3).

For composition with \(\log u\), the derivative formula uses
signed Stirling numbers \(s(n,j)\):
\[
\frac{d^n}{du^n}k(\log u)
 =u^{-n}\sum_{j=1}^n s(n,j)k^{(j)}(\log u),\qquad
|s(n,j)|\le\frac{n!}{j!}\binom{n-1}{j-1}.
\]
The inequality follows by replacing each permutation cycle by an ordered
list. Since \(u>1\) on the support and
\(\ell_j^{\kappa j}\le\ell_n^{\kappa n}\), (8) and the
binomial sum give
\[
\phi\in C_c^\infty((1,2);\mathbb C),\qquad
\|\phi^{(n)}\|_\infty\le C_\phi L^nW_n,\quad L\ge1.
\tag{9}
\]
Zero extension is smooth and obeys the same bound. The elementary
argument proves the actual composition estimate; no unverified closure
property of a named smoothness class is needed.

## 2. The reciprocal contour retains the same full pole

Termwise integration by parts in (7) is justified by its smooth-norm
convergence. Therefore
\[
\Phi(s):=\int\phi(u)u^{s-1}du=D^{-1}P(s)G(s),\qquad
G(s)=\int g(t)e^{st}dt.
\tag{10}
\]
We have \(\Phi(1)=0\), \(\Phi(\rho_0)=1\), and zeros
of full multiplicity at every unwanted point of (6).

The derivatives of \(e^{\sigma t}g(t)\) obey the same weight
bound uniformly for \(\sigma_1\le\sigma\le2\).
Integrating by parts \(n\) times and taking
\(n\) a sufficiently small fixed multiple of
\(|T|/[\log(e+|T|)]^\kappa\) gives
\[
|G(\sigma+iT)|\le
 C\exp\left[-c\frac{|T|}{[\log(e+|T|)]^\kappa}\right].
\tag{11}
\]
Indeed \(n!\le n^n\) makes the integration-by-parts bound at
most \(C(A n\ell_n^\kappa/|T|)^n\), whose base is at most
\(1/2\) for this choice.

MC-528's local division bound is independent of the bump choice:
after exact cancellation of nearby factors with their multiplicities,
\[
|P(\sigma+iT)/\zeta(\sigma+iT)|
 \le C|T|^{C_0}\exp(C_1|T|^a)
\tag{12}
\]
at sufficiently large heights, uniformly on this strip. The remaining
nearby zeros lie a fixed horizontal distance to its left. This uses
the classical local zeta factorization and power-saving density input
MC-S67/MC-S73; it does not assume an absolute sum of reciprocal residues.
Since \(|T|/(\log |T|)^\kappa\gg |T|^a\), (11) dominates
(12). The quotient \(\Phi/\zeta\) has integrable decay on
the shifted line and vanishing horizontal integrals.

Consequently the same fixed-test Mellin contour as MC-528 gives
\[
T_\phi(X):=\sum_n\mu(n)\phi(n/X)
 =X^{\rho_0}Q_{m-1}(\log X)+O_\phi(X^{\sigma_1}).
\tag{13}
\]
The polynomial has degree \(m-1\); if \(d_m\ne0\) is the
leading Laurent coefficient of \(1/\zeta\) at \(\rho_0\),
its leading coefficient is \(d_m/(m-1)!\), because
\(\Phi(\rho_0)=1\). The conjugate pole is cancelled, so no
cosine zero can suppress this complex measurement on selected scales.
Equation (13) uses one fixed test, not a contour for a moving inverse.

## 3. Bounded finite inversion at almost analytic order

For zero-extended functions put
\[
A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,\qquad
\frac{z}{1-e^{-z}}=\sum_{j\ge0}c_jz^j.
\]
The generating function is analytic for \(|z|<2\pi\), so
Cauchy's estimate on the unit circle gives \(|c_j|\le C_0\).
For an integer \(N\ge1\), set
\[
f_{h,N}=\sum_{j=0}^{N-1}c_jh^j\phi^{(j)}.
\]
Taylor expansion inside the box integral and cancellation of powers
below \(N\) give, uniformly in \(N,h\),
\[
\|A_hf_{h,N}-\phi\|_\infty
 \le h^N\|\phi^{(N)}\|_\infty
       \sum_{j<N}\frac{|c_j|}{(N-j+1)!}
 \le C_1C_\phi(Lh)^NW_N.
\tag{14}
\]
This is MC-529's finite Taylor argument, valid for every smooth target;
only its derivative envelope has changed.

Write \(\mathcal L_h=\log(e+1/h)\). For all sufficiently small
\(h>0\), choose
\[
N(h)=\left\lfloor\frac{1}{8e^\kappa Lh\mathcal L_h^\kappa}
                  \right\rfloor\ge1,
\qquad f_h=f_{h,N(h)}.
\tag{15}
\]
For \(j\ge0\),
\[
\frac{W_{j+1}}{W_j}
 =(j+1)\ell_{j+1}^\kappa
       (\ell_{j+1}/\ell_j)^{\kappa j}
 \le e^\kappa(j+1)\ell_{j+1}^\kappa.
\tag{16}
\]
Here \(\log(\ell_{j+1}/\ell_j)
\le1/[(e+j)\ell_j]\), so the last factor is at most
\(e^\kappa\). Because \(N(h)\le1/h\), (15)–(16)
bound successive ratios of \((Lh)^jW_j\), for \(j<N(h)\),
by \(1/8\). Hence
\[
\sup_{h\text{ small}}\|f_h\|_\infty<\infty,
\qquad \sup_{h\text{ small}}\|f_h\|_2<\infty.
\tag{17}
\]
All supports of \(f_h\) lie in the fixed compact set
\(\operatorname{supp}\phi\), and
\(\int f_h=\int\phi=\Phi(1)=0\).
Also \((Lh)^NW_N\le(LhN\ell_N^\kappa)^N\le8^{-N}\).
The floor in (15) changes only a prefactor for small \(h\), so
\[
\boxed{\|A_hf_h-\phi\|_\infty
 \le C\exp\left[-\frac{c}{h[\log(e+1/h)]^\kappa}\right].}
\tag{18}
\]
The inverse uses a finite polynomial of growing order; no infinite
Bernoulli series is applied across the box multiplier's zeros.

## 4. Same-block transfer, uniform range and obstruction boundary

Let \(h=H/X\). Compact support and zero integral give the exact pairing
\[
L_{X,H}:=\sum_n\mu(n)(A_hf_h)(n/X)
 =H^{-1}\int_X^{2X}(S_{X,H}(y)-m_{X,H})f_h(y/X)\,dy.
\tag{19}
\]
The coefficient of \(\mu(n)\) is
\(H^{-1}\int_{n-H}^n f_h(y/X)dy\); thus upper-endpoint-crossing
windows are included. Only \(O(X)\) integers meet the common enlarged
support. Since \(|\mu(n)|\le1\), (13) and (18) give
\[
L_{X,H}=X^{\rho_0}Q_{m-1}(\log X)+O(X^{\sigma_1})
 +O\left(X\exp\left[-\frac{c}{h[\log(e+1/h)]^\kappa}\right]\right).
\tag{20}
\]
The function \(t/[\log(e+t)]^\kappa\) is eventually increasing.
Uniformly in (2), its value at \(t=1/h\) is at least a positive
constant times
\[
\log X(\log\log X)^{r-\kappa}.
\]
Because \(r>\kappa\), the last error in (20) is smaller than
every fixed negative power of \(X\), for all sufficiently large
\(X\), with an onset independent of \(H\). Integer rounding
only decreases \(h\), so preserves this estimate.

The leading coefficient in (13) therefore forces
\(|L_{X,H}|\ge c_2X^\beta(\log X)^{m-1}\), uniformly in
(2). Finally, (17) and Cauchy–Schwarz in (19) give
\[
|L_{X,H}|^2\le XH^{-2}V_\mu(X,H)\|f_h\|_2^2,
\]
which proves (1). A pure pole of order \(m>1\) with zero ordinary
residue is still detected by its highest Laurent coefficient.

At \(H=\lfloor X/[\log X(\log\log X)^r]\rfloor\),
dividing (1) by a hypothetical ceiling \(X^{1+\varepsilon}H\)
leaves, up to a constant,
\[
X^{2\beta-1-\varepsilon}(\log X)^{2m-3}(\log\log X)^{-r}.
\tag{21}
\]
For \(0<\varepsilon<2\beta-1\) this diverges along every
unbounded set of real scales. Thus a complete centered diagonal ceiling
at this length, with every epsilon loss and constants uniform on even
one unbounded set, would imply RH. This is a consequence of the floor,
not a source of that ceiling.

The bounded source grant in the local clue permits comparison with
[[research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion|PL-473]].
The dictionary is exact: its backward box, fixed compact target and
global error norm are those of (18); the Möbius coefficient mass here
is \(O(X)\). At the box zeros,
\[
\|A_hf-\phi\|_1\ge|\widehat\phi(2\pi k/h)|\quad(k\ne0).
\]
For \(0\le r\le1\), a power-saving error at every large real
\(X\) with the rounded length above would force a Fourier envelope
\(\exp[-c|\xi|/(\log|\xi|)^r]\). The classical logarithmic
integral \(\int^\infty dt/[t(\log t)^r]\) diverges, contradicting
nonzero compact support (MC-S82). PL-473 also checks the rounding:
\(1/h=\log X(\log\log X)^r+O(X^{-1}(\log X)^2
(\log\log X)^{2r})\), and the fixed Fourier transform is Lipschitz.
Thus (18) fills precisely the previously undecided \(r>1\) part
of this family of all-real-scale norm certificates. It does not prove
that the variance floor fails for \(r\le1\).

## Prior art, controls and evidence boundary

The bump construction is classical (MC-S81, Section 3.1), and the
Fourier threshold is classical [[research/prior_art/incremental/PA-paley-wiener-ingham-logarithmic-integral|Paley–Wiener/Ingham theory]] (MC-S82,
Theorems 1.1–1.2). Bernoulli inversion is MC-S80. The local contribution
is the explicit compatibility of these ingredients with MC-528's full
reciprocal pole cancellation and the order-uniform estimates (8),
(9), (14)–(20). No new smoothness theory, uncertainty principle or
general inversion theorem is claimed. Classical Selberg-integral
converses remain the adjacent arithmetic literature (MC-S72); a prime
main-term variance theorem is not substituted for this centered signed
Möbius pairing.

- The test depends on the full hypothetical zero set. Its normalization,
  norms and onset need not be effective or uniform as \(\beta\downarrow1/2\)
  or \(r\downarrow1\). No finite zero list constructs it.
- The moment is complete over all starts in the same block. Exceptional
  starts cannot be discarded, and a center depending on the start would
  invalidate (19). All-plus coefficients have zero centered variance at
  integer lengths, but their pole at 1 cannot satisfy simultaneously
  \(\Phi(1)=0\) and \(\Phi(\rho_0)=1\).
- Both the density exponent \(a<1\) and local reciprocal division are
  required. Mere meromorphic continuation or arbitrary bounded
  coefficients do not supply (12)–(13).
- The inverse's combined norm is bounded, but its derivative order grows.
  This is not a fixed finite measurement bank or an effective acquisition
  theorem. Moving targets, several kernels, signed sampling-error estimates
  and inversion on only sparse scales are outside the obstruction used here.
- The proof is analytic. No finite computation, Lean verification,
  independent adversarial approval, external priority, unconditional
  variance improvement or RH proof is asserted.

The coherent outcome is closure of this fixed-target regularity test:
\(r>1\) is attainable with full multiplicity retained, whereas
\(0\le r\le1\) is obstructed for the stated uniform norm certificate.
Further sharpening within this already settled family does not replace
the missing independent arithmetic cancellation estimate.

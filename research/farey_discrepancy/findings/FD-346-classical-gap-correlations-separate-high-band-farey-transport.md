# FD-346 — Classical gap correlations separate high-band Farey transport

**Status:** LITERATURE+DERIVED + UNCONDITIONAL-HIGH-BAND-LIMIT + PROJECTED-TRANSPORT-NONCONVERGENCE.

The genuine Farey rank spectrum has an explicit weak limiting profile on
any fixed band bounded away from zero frequency. Its energy is of order
`log Q / Q^2`, and its density is proportional to a squared cotangent.
For FD-319's reflected four-defect reassembly, this source contribution
dominates the balanced step in the upper-half band. The resulting
conditional spectrum stays a positive total-variation distance from the
antisymmetrically projected transport comparator.

The arithmetic input is the classical fixed-lag Farey gap correlation
asymptotic, not a new cancellation estimate. This settles projected
high-band nonconvergence without determining how the source energy splits
between indices `0 mod 4` and `2 mod 4`.

## 1. Precise high-band source theorem

For integer `Q>=3`, use the genuine Farey sequence
\[
0=x_0<x_1<\cdots<x_N=1,\qquad N=\sum_{q\le Q}\varphi(q),
\quad D_k=x_k-k/N.
\]
Here `N` is even, `D_0=D_(N/2)=D_N=0`, and `D_(N-k)=-D_k`.
Define the orthonormal DST-I coefficients
\[
d_m=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(\pi mk/N),\quad 1\le m<N.
\]
For each fixed `0<alpha<1`, as `Q->infinity`, the following finite
measures on `[alpha,1]` converge weakly:
\[
\boxed{
\frac{Q^2}{\log Q}\sum_{\substack{1\le m<N\\m/N\ge\alpha}}
 d_m^2\,\delta_{m/N}
\Longrightarrow
\frac6{\pi^2}\cot^2(\pi x/2)\,\mathbf1_{[\alpha,1]}(x)\,dx.}
\tag{1}
\]
In particular, with `B_Q={m:N/2<=m<N}`,
\[
E_Q^B:=\sum_{m\in B_Q}d_m^2
\sim C_B\frac{\log Q}{Q^2},\qquad
C_B=\frac6{\pi^2}\left(\frac2\pi-\frac12\right)>0.
\tag{2}
\]
This is an asymptotic for actual **rank** coefficients at `m=Theta(N)`.
It does not substitute the position-Fourier coefficients from FD-342,
whose total-energy-relative error is insufficient at this scale.

## 2. Classical input and the spectral measure proof

Extend `x_(k+N)=x_k+1` and let `g_k=x_(k+1)-x_k`, so that `g` is
periodic of period `N`. Put
\[
S_r(Q)=\sum_{k=0}^{N-1}g_k g_{k+r}.
\]
The literature gives, with `r` fixed before taking the limit,
\[
S_0(Q)=\frac{12}{\pi^2}\frac{\log Q}{Q^2}+O(Q^{-2}),\qquad
S_1(Q)=\frac6{\pi^2}\frac{\log Q}{Q^2}+O(Q^{-2}),\qquad
S_r(Q)=O_r(Q^{-2})\quad(r\ge2).
\tag{3}
\]
These are the Hall/Boca–Cobeli–Zaharescu gap-correlation results. An
explicit primary-source formulation is Dong–Nguyen–Nguyen–Zaharescu,
*Effective Estimates for a Class of Farey Fraction Sums and Bounds for
Mundici-Type Constants*, arXiv:2606.12907v1, equation (2.2) and Theorem 2.3.
Its periodic extension is exactly the convention above. Only the leading
terms (3) are used; no uniformity for growing `r` is assumed.

Use unitary periodic Fourier transforms
\[
G_j=N^{-1/2}\sum_{k=0}^{N-1}g_k e^{-2\pi i jk/N},\qquad
F_j=N^{-1/2}\sum_{k=0}^{N-1}D_k e^{-2\pi i jk/N},
\quad\theta_j=2\pi j/N.
\]
Define a positive measure on the circle by
\[
\mu_Q=\frac{Q^2}{\log Q}\sum_{j=0}^{N-1}|G_j|^2\delta_{\theta_j}.
\]
The finite Fourier correlation identity gives
\[
\int e^{ir\theta}\,d\mu_Q(\theta)
=\frac{Q^2}{\log Q}S_r(Q).
\tag{4}
\]
Negative moments agree with positive moments. Thus (3) identifies every
limiting Fourier moment with that of
\[
d\mu(\theta)=\frac6{\pi^3}(1+\cos\theta)\,d\theta,
\qquad 0\le\theta<2\pi.
\tag{5}
\]
In particular the masses converge to `12/pi^2`. Trigonometric polynomial
density and this uniform mass bound prove `mu_Q => mu`. This step first
fixes a polynomial, uses finitely many instances of (3), and only then
approximates a continuous test function. It never inserts a growing lag
into a fixed-lag estimate.

The discrepancy is periodic and satisfies the exact difference equation
\[
D_{k+1}-D_k=g_k-1/N.
\]
For `j!=0`, it follows that
\[
G_j=(e^{i\theta_j}-1)F_j,\qquad
|F_j|^2=\frac{|G_j|^2}{4\sin^2(\theta_j/2)}.
\tag{6}
\]
The zero-frequency gap mass is `|G_0|^2=1/N`; after multiplication by
`Q^2/log Q` it tends to zero, since `N asymp Q^2`. More importantly, the
multiplier in (6) is used only away from zero, where it is bounded.
Multiplying the limit (5) there gives
\[
\frac6{\pi^3}\frac{1+\cos\theta}{4\sin^2(\theta/2)}\,d\theta
=\frac3{\pi^3}\cot^2(\theta/2)\,d\theta.
\tag{7}
\]
No statement about the full discrepancy measure near zero follows.

Reflection makes `F_j` purely imaginary, annihilates the Nyquist
coefficient, and gives
\[
d_{2j}^2=2|F_j|^2\quad(1\le j<N/2),\qquad d_m=0\quad(m\text{ odd}).
\tag{8}
\]
Restrict (7) to `pi alpha<=theta<=pi`, double it using (8), and set
`theta=pi x`. The limiting measure has no atoms at either endpoint, so
restriction to this closed band is legitimate. This proves (1).
Integration gives (2), since
\[
I:=\int_{1/2}^1\cot^2(\pi x/2)\,dx=2/\pi-1/2.
\tag{9}
\]

## 3. Source dominance in the four-defect reassembly

Now restrict to prime `Q=p>=7`, put `h=N/2` and `b=1/(2p)`, and let
`y` be the discrepancy of FD-319's reflected `BCA` reassembly.
The exact endpoint-inclusive identity from
[VIS-468](../../visual_exploration/findings/VIS-468-four-defect-farey-reassembly-preserves-source-sector.md) is
\[
y=CD+w,\qquad (CD)_k=D_{(k+h)\bmod N},
\]
where `w_k=b` for `1<=k<h`, `w_k=-b` for `h<k<N`, and `w_0=w_h=0`.
Let `a` be the antisymmetric projection of the right-endpoint transport
used in FD-319. The complete coefficient dictionary, including the fixed
boundary ranks, is
\[
\widehat y_m=\begin{cases}
0,&m\text{ odd},\\
d_m,&m\equiv0\pmod4,\\
-d_m+2b\sqrt{2/N}\cot(\theta_m/2),&m\equiv2\pmod4,
\end{cases}
\quad \theta_m=\pi m/N,
\tag{10}
\]
\[
\widehat a_m=\begin{cases}
2b\sqrt{2/N}\cos\theta_m\cot(\theta_m/2),&m\equiv2\pmod4,\\
0,&\text{otherwise}.
\end{cases}
\tag{11}
\]
These formulas can also be checked directly: the half-shift multiplies
`d_(2j)` by `(-1)^j`; the balanced step has the displayed cotangent sine
sum; and `w-a` is supported at `1,h-1,h+1,N-1`, with values
`b/2,b/2,-b/2,-b/2`. Thus its sine coefficient is
`2b sqrt(2/N) sin(theta_m)` on `m=2 mod 4`.

On `B_p`, the squared norm of `w`'s coefficients is `O(p^-2)` because
`cot(theta_m/2)<=1`. The half-shift preserves each coefficient magnitude
of `D`, so (2) and the norm triangle inequality yield
\[
Y_p:=\sum_{m\in B_p}|\widehat y_m|^2
\sim E_p^B\sim C_B\frac{\log p}{p^2}.
\tag{12}
\]
More precisely, the relative coefficient perturbation in this band is
`O((log p)^(-1/2))`. The same bound controls the total-variation distance
between the normalized squared coefficient laws of `y` and `CD` (hence
`D`). Consequently their pushforwards by `m -> m/N` have the same weak
limit, with probability density
\[
f(x)=\frac{\cot^2(\pi x/2)}I,\qquad 1/2\le x\le1.
\tag{13}
\]
In contrast, the mesh-`4/N` Riemann sum in (11) gives
\[
A_p:=\sum_{m\in B_p}|\widehat a_m|^2
\sim 2b^2 J=\frac{J}{2p^2},\qquad
J:=\int_{1/2}^1\cos^2(\pi x)\cot^2(\pi x/2)\,dx
=\frac4\pi-\frac54>0.
\tag{14}
\]
The comparator's conditional pushforward has density
\[
f_a(x)=\frac{\cos^2(\pi x)\cot^2(\pi x/2)}J.
\tag{15}
\]
Both band energies are therefore positive for every sufficiently large
prime. All normalized laws below are used on that eventual domain; no
classification of possible small-order zero cases is needed or asserted.

## 4. An explicit total-variation obstruction

Define `pi_m^B(z)=|zhat_m|^2/sum_(ell in B)|zhat_ell|^2` when the
denominator is positive. Use the fixed event
\[
T_p=\{m\in B_p:m/N\le3/4\}.
\]
The limiting laws have no boundary atoms. Equations (13)–(15) imply
\[
\boxed{
\liminf_{p\to\infty}\operatorname{TV}(\pi^{B_p}(y),\pi^{B_p}(a))
\ge\delta:=\frac{I_T}{I}-\frac{J_T}{J}>0,}
\tag{16}
\]
where the limit is over primes and
\[
I_T=\frac{2(2-\sqrt2)}\pi-\frac14,\qquad
J_T=\frac{25/4-3\sqrt2}\pi-\frac58.
\tag{17}
\]
The exact expression gives `delta approximately 0.2989471621`.
Positivity does not depend on a numerical calculation: `cos^2(pi x)`
is strictly increasing on `[1/2,1]`, so tilting the positive density
`f` by that function strictly decreases its probability of `[1/2,3/4]`.
The event bound defining total variation then proves (16). This does
not assert convergence of the entire discrete TV distance, or that the
coarse event is optimal.

The stronger coefficient-matching test in the local inherited-sector
clue also fails, with a quantified scale. From (12), (14), and the norm
triangle inequality,
\[
\frac{\|P_{B_p}(y-a)\|_2^2}{A_p}
\sim\frac{12I}{\pi^2J}\log p\longrightarrow\infty.
\tag{18}
\]
Here `P_B` denotes projection onto the named sine modes. Equation (18)
alone would not establish spectral separation after separate energy
normalizations; (16) provides that additional conclusion.

## 5. What remains unresolved and what this changes

The clue's inherited-sector ratio
\[
\eta_p=\frac{\sum_{m\in B_p,\ 4\mid m}d_m^2}{Y_p}
\]
is still not determined. The event `4|m` oscillates on the frequency
mesh, whereas (1) controls fixed continuous-frequency tests and their
continuity sets. Equivalently, separating even and odd Fourier indices
inserts `(-1)^j`, which requires correlations at lags near `N/2` rather
than the fixed lags in (3). Claiming `eta_p -> 1/2` from the weak limit
would be unjustified. A positive limit or limsup for `eta_p` is no longer
needed to rule out the projected high-band match.

The high band has energy `Theta(log Q/Q^2)`, far below the RH-critical
full Franel scale. The density (1) is an intrinsic consequence of
classical local gap correlations and discrete integration. It neither
estimates the low-frequency singular region nor improves the scalar
Franel criterion. In particular it is compatible with FD-342's
concentration below every fixed linear cutoff `m=O(Q)`, because (1)
normalizes a much smaller tail by its own scale.

The reassembly remains an artificial increasing rational grid preserving
labeled edges, not a second genuine Farey sequence. Its projected
transport is an analysis vector, not a statistically calibrated null.
The result closes that particular comparator's asymptotic matching
route; it does not supply new arithmetic cancellation or evidence for RH.

## 6. Audit, provenance, and novelty boundary

A scratch standard-library audit independently generated the exact
Farey grids for every `3<=Q<=25`. It verified periodic centered gap
integration, reflection-compatible zero mean, and 138 exact rational
identities
`sum_k (x_(k+t)-x_k)^2=t S_0+2 sum_(r=1)^(t-1)(t-r)S_r`,
for `1<=t<=6`. Direct unitary Fourier sums and independent sine sums
at `Q=7,11,19,31,43,61,101` checked (4), (6), (8), and (10)–(11),
with maximum absolute identity error below `1.1e-14`. Elementary
antiderivatives give (9), (14), and (17); numerical quadrature agreed
with the displayed constant in (16). These are finite algebra and
normalization checks, not evidence for the asymptotic theorem, which
follows from (3) and the measure argument. No Lean verification or
independent adversarial approval is claimed.

The primary arithmetic anchors are:

- Florin P. Boca, Cristian Cobeli, Alexandru Zaharescu, *A conjecture of
  R. R. Hall on Farey points*, J. reine angew. Math. **535** (2001),
  207–236, [DOI](https://doi.org/10.1515/crll.2001.049), with
  [author-institution record](https://experts.illinois.edu/en/publications/a-conjecture-of-r-r-hall-on-farey-points/).
- Anji Dong, Huy Xuan Nguyen, Vi Anh Nguyen, Alexandru Zaharescu,
  *Effective Estimates for a Class of Farey Fraction Sums and Bounds for
  Mundici-Type Constants*, [arXiv:2606.12907v1](https://arxiv.org/html/2606.12907v1),
  equation (2.2), Theorem 2.3 and the periodic convention in Section 1.
  The full displayed source statements were checked for constants,
  indexing and fixed-lag quantifiers.

Fourier autocorrelation, weak convergence via trigonometric polynomials,
and the inverse difference multiplier are classical. Targeted literature
checks covered Farey gap moments/correlations, rank power spectra and
cotangent profiles. No general Fourier or arithmetic novelty is claimed.
The line-local mathematical addition is their band-specific application:
(1) resolves the source energy at the previously uncontrolled scale,
and (16) eliminates projected transport convergence by a fixed frequency
event, independently of the unresolved residue-sector split. The
source-to-reassembly dictionary was supplied by the explicitly authorized
VIS-468 handoff and reconstructed here, rather than treating its finite
panel as asymptotic evidence.

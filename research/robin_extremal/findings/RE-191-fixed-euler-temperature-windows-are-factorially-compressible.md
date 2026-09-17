# RE-191 — Fixed Euler-temperature windows are factorially compressible

**Status:** `EXACT-DERIVED + EULER-SPECTRAL-CONDITIONING + CONSTANT-DISTANCE-WINDOW + FINITE-LAPLACE-REDUCTION + FACTORIAL-LOW-RANK + SELECTOR-SCALE + SOURCE-INFORMATION-BOUND + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-174, RE-183, RE-190.

`RE-190` shows that exact Euler samples in any shrinking `o(1)` neighborhood of `s=1` become asymptotically rank one on a fixed multiplicative selector shell. The obvious next scalar escape is to stop shrinking the spectral window and sample an entire interval a constant distance into `Re s>1`. Such an interval is exactly source-rigid by analyticity, so rank one can no longer be true.

The stable information gain is nevertheless much smaller than the continuum of samples suggests. On selector-scale support the exact Euler channel is, up to an `O(p^-1)` source-scale error, a finite Laplace transform on a compact rectangle. Its approximation numbers therefore admit an elementary factorial bound.

Fix constants

\[
0<A<B<\infty,
\qquad U>0,
\]

and let a finite signed ordinary-prime packet be supported on

\[
Ap\le q\le Bp.
\]

Write

\[
D_p(s):=\sum_q c_q\log(1-q^{-s})^{-1},
\qquad
V_p:=\sum_q\frac{|c_q|}{q},
\]

and for `0<=u<=U` normalize the constant-distance Euler profile by

\[
(\mathcal E_{p,U}c)(u)
:=p^uD_p(1+u).
\tag{1}
\]

Put

\[
\alpha_q:=\log(q/p),
\qquad
M:=\max\{ |\log A|,|\log B|\}.
\tag{2}
\]

For every integer `m>=1`, define the reciprocal log-location moments

\[
\mu_k(c):=\sum_q\frac{c_q}{q}\alpha_q^k,
\qquad 0\le k<m,
\tag{3}
\]

and the rank-at-most-`m` operator

\[
(\mathcal R_{p,U,m}c)(u)
:=\sum_{k=0}^{m-1}\frac{(-u)^k}{k!}\mu_k(c).
\tag{4}
\]

Then, for all sufficiently large `p`,

\[
\boxed{
\|\mathcal E_{p,U}-\mathcal R_{p,U,m}\|_{\ell^1(q^{-1})\to L^\infty[0,U]}
\le
 e^{UM}\frac{(UM)^m}{m!}
 +\frac{C_A}{p}.
}
\tag{5}
\]

The constant is independent of the number of primes in the packet, the sampling density in `u`, and the coefficients `c_q`.

Equivalently, if

\[
a_{m+1}(\mathcal E_{p,U})
:=
\inf_{\operatorname{rank}R\le m}
\|\mathcal E_{p,U}-R\|,
\]

then

\[
\boxed{
a_{m+1}(\mathcal E_{p,U})
\le e^{UM}\frac{(UM)^m}{m!}+O_A(p^{-1}).}
\tag{6}
\]

Thus a fixed constant-distance Euler interval has **super-exponentially compressible stable source rank**. Exact continuum data contain infinitely many coordinates, but coordinates beyond the first `m` reciprocal log-moments live below a factorial source-scale tolerance.

## 1. Exact Euler factors reduce uniformly to a compact Laplace kernel

For real `u>=0`, the Euler factor has the absolutely convergent expansion

\[
\log(1-q^{-1-u})^{-1}
=
q^{-1-u}
+
\sum_{n\ge2}\frac{q^{-n(1+u)}}n.
\tag{7}
\]

The first harmonic in the normalization (1) is exactly

\[
p^u q^{-1-u}
=
\frac1q e^{-u\alpha_q}.
\tag{8}
\]

This is the finite Laplace kernel in the bounded location coordinate `alpha_q`.

The prime-power completion is uniformly lower order. For `p` large enough that `p/q^2<1` throughout the shell,

\[
\begin{aligned}
p^u
\sum_{n\ge2}\frac{q^{-n(1+u)}}n
&\ll
p^u q^{-2(1+u)}\\
&=
q^{-2}\left(\frac{p}{q^2}\right)^u\\
&\le q^{-2}.
\end{aligned}
\tag{9}
\]

Therefore

\[
\boxed{
\sup_{0\le u\le U}
\left|
(\mathcal E_{p,U}c)(u)
-
\sum_q\frac{c_q}{q}e^{-u\alpha_q}
\right|
\ll_A \frac{V_p}{p}.
}
\tag{10}
\]

Unlike `RE-190`, no shrinking-window hypothesis is used here. The `O(p^-1)` prime-power remainder is uniform on every one-sided window `u>=0`; the new issue is the nontrivial Laplace dependence `e^{-u alpha}` that survives when `U=Theta(1)`.

## 2. Taylor separation gives a factorial rank bound

For `0<=u<=U` and `|alpha|<=M`, Taylor's theorem gives

\[
\left|
e^{-u\alpha}
-
\sum_{k=0}^{m-1}\frac{(-u\alpha)^k}{k!}
\right|
\le
 e^{UM}\frac{(UM)^m}{m!}.
\tag{11}
\]

Multiplying by `|c_q|/q`, summing over the packet, and using (10) yields

\[
\sup_{0\le u\le U}
\left|
(\mathcal E_{p,U}c)(u)
-
\sum_{k=0}^{m-1}\frac{(-u)^k}{k!}\mu_k(c)
\right|
\le
\left[
 e^{UM}\frac{(UM)^m}{m!}
 +\frac{C_A}{p}
\right]V_p.
\tag{12}
\]

The range of the approximating operator is contained in the `m`-dimensional polynomial space spanned by `1,u,...,u^(m-1)`, proving (5)--(6).

There is a useful basis-free consequence. Let `S` be any `(m+1)`-dimensional linear subspace of the finite packet coefficient space. Since `R_(p,U,m)|_S` has a nontrivial kernel, there exists nonzero `c in S` such that

\[
\boxed{
\|\mathcal E_{p,U}c\|_\infty
\le
\left[
 e^{UM}\frac{(UM)^m}{m!}
 +\frac{C_A}{p}
\right]
\|c\|_{p,1}.
}
\tag{13}
\]

Hence no matter how densely the interval is sampled, every source subspace of dimension `m+1` contains a direction invisible above the tolerance on the right of (13). This is a stable-rank statement, not merely a convenient polynomial approximation of one packet.

## 3. Fixed precision needs only finitely many source coordinates

For fixed `A,B,U`, Stirling gives

\[
 e^{UM}\frac{(UM)^m}{m!}
\le
 e^{UM}
\left(\frac{eUM}{m}\right)^m.
\tag{14}
\]

Let `epsilon_p->0` with

\[
p^{-1}=o(\epsilon_p).
\tag{15}
\]

Writing `L_p=log(1/epsilon_p)`, one may choose

\[
\boxed{
m_p
\le
(1+o(1))\frac{L_p}{\log L_p}}
\tag{16}
\]

so that the right side of (5) is at most `epsilon_p`. In particular, for every **fixed** source-scale tolerance `epsilon>0`, the entire continuum `u in [0,U]` is approximable to error `epsilon` by a rank bounded independently of `p` and independently of the number of available selector-shell primes.

The inverse interpretation is the one relevant to source information. To force more than `m` robust scalar directions from a fixed spectral interval, one must work below a tolerance no larger than roughly

\[
\frac{(UM)^m}{m!}
\tag{17}
\]

before the `O(p^-1)` prime-power floor of this first-harmonic reduction matters. Merely increasing the number of exact sample points cannot change that conditioning scale.

## 4. RE-190 is the rank-one endpoint of the same law

Take a shrinking window

\[
U_p=\frac{T_p}{\log p}=o(1)
\]

and set `m=1`. Then (5) gives

\[
\|\mathcal E_{p,U_p}-\mathbf 1\otimes\mu_0\|
\ll_{A,B}
U_p+\frac1p,
\tag{18}
\]

where

\[
\mu_0(c)=\sum_q\frac{c_q}{q}.
\]

Since `p^u=e^tau` when `u=tau/log p`, this is exactly the one-sided `Re s>=1` version of the reciprocal-mass rank-one collapse in `RE-190`. The present finding therefore does not replace that result; it extends its geometry from

\[
U_p=o(1),\quad \text{stable rank }1,
\]

to

\[
U=Theta(1),\quad
\text{stable rank growing only factorially with requested precision}.
\]

This makes the scalar frontier more continuous than a simple rank-one-versus-full-rank dichotomy.

## 5. Exact rigidity and stable information are different

A nontrivial real interval of exact Euler values is still an exact source fingerprint. If

\[
D_p(1+u)=0
\qquad(0\le u\le U)
\]

for a finite packet, analyticity forces the discrepancy to vanish identically in its half-plane of analyticity, after which the first-defect argument of `RE-174` gives `c_q=0` for every prime. The same identity-theorem principle applies to absolutely convergent infinite bounded-multiplicity discrepancies on `Re s>1`.

There is therefore no contradiction between exact rigidity and (5). Recovering the extra source coordinates requires resolving the factorially small residual left after the low-rank Laplace approximation. `RE-183` lies on the other side of the same distinction: every fixed **finite** temperature panel can be matched exactly by honest ordinary-prime `{0,1,2}` controls with a transient Robin excursion, whereas a whole interval cannot be matched exactly by a nontrivial source.

The present result does **not** construct an honest `{0,1,2}` control whose whole constant-distance interval is approximately matched at the factorial tolerance. Equation (13) uses arbitrary real signed directions in coefficient space. Its conclusion is an observable-conditioning bound: a fixed interval does not automatically provide a large number of robust source coordinates merely because it contains continuum-many exact values.

## 6. Consequence for the current scalar frontier

`RE-190` left constant-distance spectral probes as the most immediate scalar escape from shrinking-window collapse. They do escape rank one, but the escape is quantitatively weak at finite precision. For selector-shell packets the stable source content of `[1,1+U]` is controlled by reciprocal log-location moments, and the number of moments needed at tolerance `epsilon` grows only like

\[
\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}
\]

above the `p^-1` first-harmonic floor.

Accordingly, a future Robin argument based on a fixed constant-distance Euler interval must specify the precision at which those values are source-native. Exact analyticity is not enough: if the available arithmetic input controls the interval only to a natural error much larger than the factorial tail, most of the exact source rank is unusable. A genuinely stronger scalar route would need either a precision theorem that survives this compression, a spectral span `U=U_p` growing with the selector, logarithmically separated source scales that enlarge the `alpha`-diameter, or a joint/nonlocal invariant tied directly to the Robin destination.

## 7. Adversarial and representation audit

**The theorem is an upper bound on stable rank, not a matching lower bound.** The true approximation numbers may decay even faster. No claim is made that the factorial scale in (5) is sharp for the exact Euler operator.

**The coefficient direction in (13) is relaxed.** It need not have entries in `{-1,0,1}`. Honest bounded-multiplicity matched-control non-rigidity still requires a separate quantization construction, as in `RE-181`--`RE-188`.

**The support diameter is load-bearing.** The constant `M` is the logarithmic radius of the selector shell. If the packet spans `q` over powers of `p`, then `M=Theta(log p)` and a fixed spectral interval can carry many more stable coordinates. This is exactly the multi-scale escape already left open by `RE-190`.

**Unbounded temperatures are outside the fixed-window conclusion.** If `U=U_p->infinity`, the bound remains formally true with `UM` in place of a constant but requires growing rank. This is compatible with the exact unbounded-temperature rigidity of `RE-174`.

After the selector-scale normalization, the core kernel `e^{-u alpha}` is the classical finite Laplace transform, so factorial/super-exponential compressibility is not claimed as a new theorem of approximation theory. Nearby prior art includes R. R. Lederman and V. Rokhlin, *On the Analytical and Numerical Properties of the Truncated Laplace Transform I*, SIAM Journal on Numerical Analysis **53** (2015), 1214--1235, DOI `10.1137/140990681`, and N. Bourguiba and A. Karoui, *Weighted finite Laplace transform operator: spectral analysis and quality of approximation by its eigenfunctions*, Integral Transforms and Special Functions **29** (2018), 679--698, DOI `10.1080/10652469.2018.1489804`, which proves super-exponential eigenvalue decay for a weighted finite bilateral Laplace operator. The line-specific content here is the uniform reduction of the **exact Euler-factor channel** to that compact Laplace geometry at selector scale, including the prime-power `O(p^-1)` remainder and the direct bridge from `RE-190` to constant-distance sampling. The proof above is self-contained and imports no load-bearing theorem from that literature, so `SOURCES.md` requires no new dependency.

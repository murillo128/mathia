# PC-161 — one-hole puncture defect has a prime-blind trace-class star limit

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for interpreting the sparse macroscopic eigenvalues of the PC-158 one-hole puncture **defect operator itself**, at fixed base conductor, as new-prime-specific spectral data. PC-158 determined the exact trace/Schatten-1 budget of this defect and showed that only `O(phi(d))` eigenvalue positions can move macroscopically when a new prime is adjoined, but it deliberately left the organization of those sparse modes open. The full defect spectrum has a stronger classification: along every coprime fiber size, prime or composite, it converges in `l^1` to a fixed direct sum of trace-class inverse-square stars determined only by the base residue pattern.

Fix `d>=2`, put `r=phi(d)`, and let `m>=2` satisfy `(m,d)=1`. As in PC-158, define

\[
S_{d,m}:=\{x\bmod dm:(x,d)=1\},
\qquad
O_{d,m}:=\{x\in S_{d,m}:m\mid x\},
\]

and

\[
X_{d,m}:=S_{d,m}\setminus O_{d,m}.
\]

There is one point of `O_{d,m}` in every coarse fiber, so `|O_{d,m}|=r`. When `m=q` is a prime not dividing `d`, `X_{d,q}=U(dq)` is the genuine new primitive shell. Let

\[
K_{d,m}
:=\frac1{(dm)^2}
\sum_{\substack{\{x,y\}\subset S_{d,m}\\
\{x,y\}\cap O_{d,m}\ne\varnothing}}
\frac{(e_x-e_y)(e_x-e_y)^*}
{4\sin^2\!\bigl(\pi(x-y)/(dm)\bigr)}.
\tag{1}
\]

This is exactly the positive puncture defect of PC-158, so for prime `q`

\[
K_{d,q}=M_{d,q}-(A_{dq}\oplus0_r)\succeq0.
\]

For `a in U(d)` define the infinite allowed offset set

\[
E_a:=\{h\in\mathbb Z\setminus\{0\}:(a+h,d)=1\},
\tag{2}
\]

and on `l^2({0} sqcup E_a)` define the weighted star Laplacian

\[
\mathcal K_a
:=\sum_{h\in E_a}
\frac1{4\pi^2h^2}
(e_0-e_h)(e_0-e_h)^*.
\tag{3}
\]

The canonical fixed-base limit is

\[
\boxed{
\mathcal K_{d,\infty}:=
\bigoplus_{a\in U(d)}\mathcal K_a.
}
\tag{4}
\]

Every summand in (3) is positive rank one and has trace `2/(4 pi^2 h^2)`. Hence (4) is positive trace class. If

\[
\lambda_1(T)\ge\lambda_2(T)\ge\cdots\ge0
\]

denotes the eigenvalues of a positive compact operator, with finite lists padded by zeros, then

\[
\boxed{
\lim_{\substack{m\to\infty\\(m,d)=1}}
\sum_{j\ge1}
\left|
\lambda_j(K_{d,m})-\lambda_j(\mathcal K_{d,\infty})
\right|=0.
}
\tag{5}
\]

Thus every fixed-index order-one defect eigenvalue has a limit that is independent of whether the refining integer is prime. For a genuinely new prime `q`, the sparse spectrum left open by PC-158 is therefore not a new-prime spectral family: it is one subsequence of a universal coprime one-hole star limit.

## 1. A bounded chord window is exactly a disjoint union of local stars

Represent differences modulo `dm` by centered integers. For `H>=1`, let `K_{d,m}^{(H)}` be the part of (1) containing only edges whose centered difference `h` satisfies `0<|h|<=H`.

Every old point has the form

\[
y=mb,
\qquad b\in U(d).
\tag{6}
\]

Its residue modulo `d` is

\[
a\equiv mb\pmod d,
\tag{7}
\]

and multiplication by `m` permutes `U(d)`. A nearby point `y+h` belongs to `S_{d,m}` exactly when

\[
(y+h,d)=1
\quad\Longleftrightarrow\quad
(a+h,d)=1.
\tag{8}
\]

If `m>2H`, two distinct old points cannot be within centered distance `2H`: their difference is a nonzero multiple of `m` modulo `dm`. Moreover no nonzero `|h|<=H` can carry an old point to another old point. Consequently the short-edge neighborhoods of the old section are disjoint, and after the permutation (7) the finite operator is **exactly**

\[
\boxed{
K_{d,m}^{(H)}
\simeq
\bigoplus_{a\in U(d)}
\sum_{\substack{0<|h|\le H\\(a+h,d)=1}}
 w_{d,m}(h)(e_0-e_h)(e_0-e_h)^*,
}
\tag{9}
\]

where

\[
w_{d,m}(h)
:=
\frac1{4d^2m^2\sin^2(\pi h/(dm))}.
\tag{10}
\]

For each fixed nonzero `h`,

\[
\boxed{
w_{d,m}(h)\longrightarrow\frac1{4\pi^2h^2}.}
\tag{11}
\]

Therefore for fixed `H`, after identifying the finitely many star coordinates in (9),

\[
\boxed{
\left\|K_{d,m}^{(H)}-
\mathcal K_{d,\infty}^{(H)}\right\|_1
\longrightarrow0,
}
\tag{12}
\]

where `mathcal K_{d,infinity}^{(H)}` is (4) truncated to `|h|<=H`. No primality, primitive-order identity, Möbius weight, or zeta input appears in this local limit. The only arithmetic datum is the fixed reduced-residue mask modulo `d`.

## 2. The long-chord remainder is uniformly trace-class

For a centered difference satisfying `0<|h|<=dm/2`, the elementary concavity bound

\[
\sin\frac{\pi|h|}{dm}
\ge\frac{2|h|}{dm}
\]

gives

\[
\boxed{
w_{d,m}(h)\le\frac1{16h^2}.}
\tag{13}
\]

Every edge term `w(e_x-e_y)(e_x-e_y)^*` has trace norm `2w`. Summing the omitted incident edges separately from each of the `r` old vertices can only overcount old-old edges, so

\[
\begin{aligned}
\left\|K_{d,m}-K_{d,m}^{(H)}\right\|_1
&=\operatorname{Tr}\left(K_{d,m}-K_{d,m}^{(H)}\right)\\
&\le
2r\sum_{|h|>H}\frac1{16h^2}
\le\frac{r}{4H}.
\end{aligned}
\tag{14}
\]

The limiting stars have the analogous bound

\[
\boxed{
\left\|\mathcal K_{d,\infty}
-\mathcal K_{d,\infty}^{(H)}\right\|_1
\le\frac{r}{\pi^2H}.
}
\tag{15}
\]

The key point is that the control is uniform in the fiber size. The finite puncture may have `rm` ambient coordinates, but all of its order-one trace-class mass remains in bounded neighborhoods of the `r` deleted points; the aggregate long-chord tail is summable.

Old-old edges cause no hidden exception. For fixed `H<m/2` none occur in (9), while all of them are included in the uniformly controlled remainder (14). In fact there are only `O_d(1)` such edges and their normalized weights are `O_d(m^{-2})`, but that sharper estimate is not needed.

## 3. Trace-norm localization gives `l^1` convergence of the complete defect spectrum

For self-adjoint trace-class operators, the standard Lidskii/Mirsky eigenvalue stability inequality gives

\[
\sum_j|\lambda_j(A)-\lambda_j(B)|
\le\|A-B\|_1
\tag{16}
\]

when the eigenvalues are ordered consistently and zero-padded. Apply (16) first to the fixed-window identification (12), then to the finite and infinite tails. From (12)--(15),

\[
\limsup_{\substack{m\to\infty\\(m,d)=1}}
\sum_j
|\lambda_j(K_{d,m})-\lambda_j(\mathcal K_{d,\infty})|
\le
\frac{r}{4H}+rac{r}{\pi^2H}.
\tag{17}
\]

Letting `H->infinity` proves (5).

This is stronger than convergence of empirical spectral measure. The dimension of the finite ambient space diverges, yet the complete nonzero defect spectrum converges as an `l^1` sequence. In particular, any finite number of largest eigenvalues, any fixed spectral threshold away from a limiting eigenvalue, and every Schatten moment controlled by the trace-class mass are asymptotically determined by the fixed base stars rather than by prime birth.

## 4. The limiting trace recovers the PC-158 reduced-residue factor

PC-158 gives the exact finite trace

\[
\operatorname{Tr}K_{d,m}
=
\frac r{12}
\left[
2\rho_d-
\frac{\rho_d+d^{-2}}{m^2}
\right],
\qquad
\rho_d:=\prod_{p\mid d}
\left(1-\frac1p-\frac1{p^2}\right).
\tag{18}
\]

Equation (5), or directly dominated convergence in the star representation, therefore gives

\[
\boxed{
\operatorname{Tr}\mathcal K_{d,\infty}
=\frac{r\rho_d}{6}.
}
\tag{19}
\]

Combining (3)--(4) with (19) yields the equivalent exact reduced-residue series

\[
\boxed{
\sum_{a\in U(d)}
\sum_{\substack{h\in\mathbb Z\setminus\{0\}\\(a+h,d)=1}}
\frac1{h^2}
=
\frac{\pi^2r\rho_d}{3}.
}
\tag{20}
\]

Thus even the total mass of the trace-class star limit is the same classical two-point reduced-residue factor already exposed by PC-158. Equation (20) is a consistency identity, not a new zeta bridge.

## 5. Matched composite control removes the new-prime interpretation

The proof used only `(m,d)=1`. For composite `m`, `X_{d,m}` is generally **not** the primitive shell `U(dm)` because deleting the single residue `0 mod m` does not remove points divisible by proper prime factors of `m`. This is exactly the matched control introduced in PC-158: the ambient root geometry, one deleted section per coarse fiber, inverse-square chord rule, and normalization are preserved while prime birth is removed.

Equation (5) holds along this entire coprime integer family. Hence the prime subsequence has no distinct limiting defect eigenvalues, multiplicity law, or trace-class spectral mass. The local stars remember the base reduced-residue mask but do not detect whether the new fiber cardinality was prime.

This rules out the specific route

\[
\boxed{
\text{new-prime one-hole puncture}
\longrightarrow
\text{sparse spectrum of }K_{d,q}
\longrightarrow
\text{prime-specific/RH spectral data}
}
\]

at fixed base conductor. It materially sharpens PC-158: the sparse defect modes are not merely few; the **entire defect spectrum** is asymptotically a fixed prime-blind local object.

The statement is intentionally narrower than a classification of the punctured primitive operator. It does **not** determine how the eigenvectors of `K_{d,m}` sit relative to the Bloch eigenvectors of the ambient operator `M_{d,m}`, and therefore does not by itself classify the spectrum of `M_{d,m}-K_{d,m}` beyond PC-157/PC-158. It also does not cover simultaneous growth of the base conductor `d`, growing-support or renormalized cross-level observables, nonlinear couplings between conductors, or the global uniformization/monodromy branch. Those require information not contained in the unordered spectrum of the one-hole defect alone.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. The regular-polygon inverse-square/cosecant kernel is already anchored for Prime Circle by Calogero--Perelomov. The trace-class step uses standard trace-ideal and eigenvalue-stability theory; a canonical reference is Barry Simon, **Trace Ideals and Their Applications**, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), especially the trace/Lidskii framework. Michael Farber and Lewin Strauss, **Spectra of infinite graphs with summable weight functions**, arXiv:2206.07688 (2022), studies Laplacians of infinite weighted graphs under summability of the edge weights and provides a modern neighboring setting for the infinite stars in (3).

Directed searches across punctured roots-of-unity `csc^2` Laplacians, inverse-square cyclic defects, summable weighted stars, and trace-class graph limits did not locate the exact fixed-base one-hole limit (4)--(5). That absence is not evidence of historical priority, and no new general theorem about trace ideals or infinite weighted graphs is claimed. The durable content is the line-specific reduction: the sparse PC-158 defect spectrum, which was the remaining spectral loophole of the one-hole mechanism, localizes to a canonical `1/h^2` star object that survives unchanged on the matched composite family.

## 7. Falsification surface

The result has several direct failure tests. For fixed `H` and any `m>2H`, one collision between two short old-point neighborhoods would falsify the exact direct-sum representation (9). One allowed short edge whose residue condition differs from (8) would falsify the base-mask identification. A sequence of coprime `m` for which the long-edge trace exceeds the uniform `O(1/H)` bound would break the trace-class localization. Finally, any fixed base `d` for which the zero-padded eigenvalue lists fail to approach (4) in `l^1` would falsify (5).

The surviving spectral question is therefore relational rather than defect-scalar: whether the **joint orientation/coupling** of the puncture defect with the ambient Bloch operator retains arithmetic information even though the defect's own spectrum does not. Treating isolated eigenvalues of `K_{d,q}` alone as unexplained new-prime spectral data is no longer justified.
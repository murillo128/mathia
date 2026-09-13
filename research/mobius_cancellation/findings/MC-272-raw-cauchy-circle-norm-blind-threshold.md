# MC-272 — Raw Cauchy circle norms stay above the blind-atom threshold

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-energy polynomial from `MC-271`,

\[
G(z)=\sum_{j=0}^{N}F_jz^j,
\qquad
F_j=\sum_{\substack{T\subseteq\mathcal R_y\\|T|=j}}
\left|\sum_{S\in\mathcal B_m}\chi_T(q_S)\right|^2,
\tag{1}
\]

with

\[
Z=|\mathcal B_m|,
\qquad
F_0=Z^2.
\tag{2}
\]

`MC-271` left complex Cauchy extraction open because angular phase can cancel even though every coefficient `F_j` is nonnegative. The first natural complex escape is therefore to recover `F_t` from a circle and then estimate the circle by an absolute `L^p` or Hardy norm.

That entire raw-norm route still misses the blind scale.

For `r>0` and `1\le p\le\infty`, use normalized circle measure and write

\[
\|G_r\|_p
=
\left(\frac1{2\pi}\int_0^{2\pi}
|G(re^{i\theta})|^p\,d\theta\right)^{1/p},
\tag{3}
\]

with the usual supremum interpretation for `p=\infty`. Cauchy/Fourier coefficient extraction gives

\[
F_t r^t
=
\left|
\frac1{2\pi}\int_0^{2\pi}
G(re^{i\theta})e^{-it\theta}\,d\theta
\right|
\le \|G_r\|_1
\le \|G_r\|_p.
\tag{4}
\]

Thus the raw norm certificate is

\[
\mathcal C_p(r):=r^{-t}\|G_r\|_p.
\tag{5}
\]

Let

\[
A:=\frac{2^N}{Z(N+1)}.
\tag{6}
\]

Then, whenever `A\ge1`, every subunit radius obeys

\[
\boxed{
\frac{\mathcal C_p(r)}{Z^2}
\ge
\max\{r^{-t},A r^{N-t}\},
\qquad 0<r\le1,
}
\tag{7}
\]

and hence

\[
\boxed{
\inf_{0<r\le1}
\frac{\mathcal C_p(r)}{Z^2}
\ge A^{t/N}.
}
\tag{8}
\]

On the superunit side, let

\[
d_*:=\max\{j:F_j>0\}.
\]

The sparse-support argument in `MC-271` gives

\[
d_*\ge N-\log_2 Z.
\tag{9}
\]

Since a nonzero `F_{d_*}` is a positive integer, for `r\ge1`

\[
\boxed{
\frac{\mathcal C_p(r)}{Z^2}
\ge
\max\left\{
A r^{-t},
\frac{r^{d_*-t}}{Z^2}
\right\}.
}
\tag{10}
\]

When `d_*>t`, optimizing the two monotone terms yields

\[
\boxed{
\inf_{r\ge1}
\frac{\mathcal C_p(r)}{Z^2}
\ge
A\left(\frac{2^NZ}{N+1}\right)^{-t/d_*}.
}
\tag{11}
\]

At the live Christoffel choice

\[
m=t+1,
\qquad
t=\left(\frac1{\log2}+o(1)\right)\log\log y,
\qquad
N\asymp\frac y{\log y},
\tag{12}
\]

`MC-271` already gives

\[
\log Z=o(N),
\qquad
d_*=N-o(N),
\qquad t=o(N).
\tag{13}
\]

Therefore

\[
\log A=(\log2-o(1))N,
\tag{14}
\]

so the subunit floor is

\[
\boxed{
A^{t/N}
=\exp((\log2-o(1))t)
=(\log y)^{1+o(1)}.
}
\tag{15}
\]

The superunit floor in `(11)` is much larger:

\[
\boxed{
A\left(\frac{2^NZ}{N+1}\right)^{-t/d_*}
=\exp((\log2-o(1))N).
}
\tag{16}
\]

Combining `(8)` and `(11)`, uniformly for every `1\le p\le\infty`,

\[
\boxed{
\inf_{r>0}
\frac{r^{-t}\|G(re^{i\theta})\|_{L^p(d\theta/2\pi)}}{Z^2}
\ge
(\log y)^{1+o(1)}.
}
\tag{17}
\]

Thus **complex circles do not rescue the raw generating polynomial once angular phase is discarded into any ordinary `L^p` norm**. The best possible Cauchy-plus-circle-norm certificate is asymptotically larger than the contribution `Z^2` of one blind row by a logarithmic factor, despite allowing the radius to vary arbitrarily.

This closes the most immediate complex-contour escape left by `MC-271`. A viable complex method must keep the signed Fourier phase all the way to the target frequency, or first subtract/cancel substantial known shell content before taking absolute norms. Merely replacing a positive-real majorant by a Hardy/circle norm is not enough.

No blind relation is excluded, no estimate of `F_t` is proved, and no new bound for `M(X)` follows.

## 1. Every coefficient and the total positive mass force circle-norm lower bounds

For each `0\le j\le N`, Fourier inversion on the radius-`r` circle gives

\[
F_jr^j
=
\left|
\frac1{2\pi}\int_0^{2\pi}
G(re^{i\theta})e^{-ij\theta}\,d\theta
\right|
\le\|G_r\|_1
\le\|G_r\|_p.
\tag{18}
\]

Summing the coefficientwise inequalities gives the elementary finite-degree evaluation bound

\[
G(r)=\sum_{j=0}^NF_jr^j
\le (N+1)\|G_r\|_p.
\tag{19}
\]

This is intentionally cruder than specialized Hardy-space estimates; its strength here comes from the enormous total coefficient mass forced by the sparse Walsh object.

`MC-271` proved by Walsh Parseval that

\[
G(1)\ge2^NZ.
\tag{20}
\]

If `0<r\le1`, then `r^j\ge r^N` for every `0\le j\le N`, so positivity of the coefficients gives

\[
G(r)
\ge r^NG(1)
\ge r^N2^NZ.
\tag{21}
\]

Equations `(19)` and `(21)` imply

\[
\|G_r\|_p
\ge\frac{2^NZ}{N+1}r^N.
\tag{22}
\]

Meanwhile `(18)` at `j=0` gives

\[
\|G_r\|_p\ge F_0=Z^2.
\tag{23}
\]

Multiplying by `r^{-t}/Z^2` yields `(7)`.

The first term in `(7)` decreases with `r`, while the second increases because `N>t`. Their crossing is

\[
r_-=A^{-1/N},
\tag{24}
\]

which lies in `(0,1]` when `A\ge1`. At that radius both terms equal `A^{t/N}`, proving `(8)`.

The key point is that moving the contour inward does suppress the huge high-shell mass, but doing so amplifies the target coefficient by `r^{-t}`. The optimum balance occurs near radius `1/2`, not near radius one, and its unavoidable cost is essentially `2^t`.

## 2. Moving the contour outward is exponentially worse

For `r\ge1`, coefficient positivity gives

\[
G(r)\ge G(1)\ge2^NZ,
\]

so `(19)` implies

\[
\frac{\mathcal C_p(r)}{Z^2}
\ge A r^{-t}.
\tag{25}
\]

On the other hand, `(18)` at the highest occupied degree gives

\[
\|G_r\|_p
\ge F_{d_*}r^{d_*}
\ge r^{d_*},
\tag{26}
\]

because `F_{d_*}` is a nonzero integer. This yields the second term in `(10)`.

When `d_*>t`, the two lower bounds in `(10)` cross at

\[
r_+^{d_*}=AZ^2
=\frac{2^NZ}{N+1}.
\tag{27}
\]

The left term decreases and the right term increases, so the minimum of their maximum occurs at `(27)`, which proves `(11)`.

The degree-support theorem used by `MC-271` says

\[
d_*\ge N-\log_2Z=N-o(N).
\]

Hence the radius `(27)` is asymptotically close to `2`, while the certificate remains exponentially large in `N`. Outward contour motion therefore cannot trade enough `r^{-t}` decay against the forced far-shell Fourier mass.

## 3. Live-scale asymptotics

At `m=t+1` with `t=O(\log\log y)` and `k_y,N_y\asymp y/\log y`, the Hamming-ball size satisfies

\[
\log Z
=O\!\left(m\log\frac{k_y}{m}+m\right)
=O((\log\log y)\log y)
=o(N).
\tag{28}
\]

Therefore `(14)` follows immediately. Then

\[
\log A^{t/N}
=\frac tN\big(N\log2-\log Z-\log(N+1)\big)
=(\log2-o(1))t.
\tag{29}
\]

Substituting the live value of `t` gives

\[
(\log2-o(1))t
=(1+o(1))\log\log y,
\]

which proves `(15)`.

For `(16)`, take logarithms in `(11)`:

\[
\log A
-\frac t{d_*}
\log\left(\frac{2^NZ}{N+1}\right).
\tag{30}
\]

The first term is `(\log2-o(1))N`, while `t/d_*=o(1)` and the logarithm in the second term is `O(N)`. Thus the second term is `o(N)`, proving `(16)`.

The global optimum is consequently on the inward side and still pays `(\log y)^{1+o(1)}` above one blind atom.

## 4. Exact phase representation and what remains open

The same Krawtchouk generating function used throughout `MC-267`--`MC-271` gives an exact representation of the complex polynomial. If

\[
d(S\triangle U)
=\#\left\{r\in\mathcal R_y:
\left(\frac{q_{S\triangle U}}r\right)=-1\right\},
\]

then

\[
\boxed{
G(z)
=\sum_{S,U\in\mathcal B_m}
(1+z)^{N-d(S\triangle U)}
(1-z)^{d(S\triangle U)}.
}
\tag{31}
\]

Indeed the coefficient of `z^j` in the pair `(S,U)` term is exactly the Krawtchouk value `K_j(d(S\triangle U);N)`, and summing pairs recovers `F_j`.

On the imaginary axis `z=i\tau`, the two factors have equal modulus. Writing

\[
\omega_\tau
=\frac{1-i\tau}{1+i\tau},
\qquad |\omega_\tau|=1,
\]

one gets

\[
G(i\tau)
=(1+i\tau)^N
\sum_{S,U\in\mathcal B_m}
\omega_\tau^{d(S\triangle U)}.
\tag{32}
\]

So complex evaluation really does expose a phase-sensitive Fourier transform of the arithmetic pair-distance distribution. Equation `(17)` does **not** say that this phase is useless. It says that taking an `L^p` magnitude of the full degree-`N` polynomial before isolating the target frequency washes out precisely the cancellation that could make `(32)` useful.

The surviving complex routes are therefore narrower:

- estimate the target Fourier coefficient with phase retained rather than bounding it by a circle norm;
- derive a signed transform that cancels large irrelevant shell mass before absolute values are taken;
- subtract sufficiently many shell contributions using independent arithmetic information before applying a norm estimate.

The last option is not a formal loophole for free. Once lower or upper shells are removed, the argument has imported shell-specific information beyond the raw generating polynomial, which is exactly the kind of new arithmetic input the current frontier requires.

## 5. Prior art and novelty boundary

Cauchy's coefficient formula, Fourier coefficient domination by the `L^1` norm, monotonicity of normalized `L^p` norms for `p\ge1`, and the interpretation of analytic boundary norms as Hardy-space norms are classical. Peter L. Duren, *Theory of H^p Spaces* (Academic Press, 1970), is a standard reference for the Hardy-space framework. No novelty is claimed for these analytic ingredients.

The Krawtchouk generating function behind `(31)` is likewise classical. NIST DLMF §18.23.3 records the standard Krawtchouk generating function; at `p=1/2` it is the same `(1-z)^d(1+z)^{N-d}` polynomial used here, up to the conventional normalization: https://dlmf.nist.gov/18.23#E3.

A targeted literature search through 13 September 2026 did not identify this exact raw-circle-norm obstruction for the Mathia sparse Legendre-syndrome shell energy. That absence is not evidence of novelty. The durable contribution is the frontier consequence inside the current arithmetic object: after positive real Poissonization fails in `MC-271`, ordinary complex Cauchy extraction followed by an absolute circle norm also cannot approach the blind atom; it loses at least a logarithmic factor at the live shell depth.

## 6. Boundaries and updated frontier

- The obstruction applies to the **raw** polynomial `G` and any proof that bounds its target coefficient by `r^{-t}\|G_r\|_p` for `1\le p\le\infty` before exploiting angular phase.
- It does not block exact Fourier extraction, oscillatory integral estimates retaining the factor `e^{-it\theta}`, signed contour identities, or other phase-sensitive estimates.
- It does not block subtracting known shell coefficients before norming. Such subtraction is additional shell-specific information and must be audited on its own merits.
- The lower bound uses only `F_0=Z^2`, the total-mass inequality `G(1)\ge2^NZ`, and the sparse-support degree floor `d_*\ge N-\log_2Z`; it does not use unproved pseudorandomness of Legendre symbols.
- The result is independent of the choice of `p\ge1`; changing among ordinary Hardy/circle norms cannot rescue the raw transform.
- No statement is made about the actual size of `F_t`.

Together with `MC-269`--`MC-271`, this leaves a sharply source-specific frontier. Layerwise absolute values require impossible precision, coefficient-uniform operator norms hit the blind atom, positive shell majorants fail, and raw complex circle norms still sit a logarithmic factor above the atom. Any surviving analytic route must now preserve **signed fixed-shell phase information before norm relaxation**, rather than hoping that a more flexible scalar norm of the same shell polynomial will create the missing cancellation.
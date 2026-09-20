# MC-414 — Collective shift-position kernel is endpoint-separable

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the incomplete translated-correlation frontier isolated by `MC-413`. For a primitive Dirichlet character `chi` of conductor `q`, that finding shows that after one additive differencing step each compatible divisor pair `(d,e)` produces an incomplete correlation

\[
\sum_{k\in I_{d,e}}
\chi(k+u_{d,e}+h[d,e]^{-1})
\overline{\chi(k+u_{d,e})},
\tag{1}
\]

with all inverses taken modulo `q`, while complete conductor blocks collapse to the Ramanujan scalar `c_q(h)`.

There is a second exact compression that appears as soon as the differencing shift is kept as a **joint summation variable** rather than frozen. Write

\[
g=(d,e),\qquad d=gd_0,\qquad e=ge_0,\qquad (d_0,e_0)=1.
\tag{2}
\]

The compatibility condition `(d,e)|h` gives `h=gj`, and every surviving pair in `MC-413` has `(de,q)=1`, hence `(g,q)=1`. Since `e|n`, also `g|n`; writing `n=gm` gives the exact identity

\[
\boxed{
\chi(n+h)\overline{\chi(n)}
=
\chi(m+j)\overline{\chi(m)}.
}
\tag{3}
\]

The divisor pair has disappeared completely from the **source-character kernel**. It remains only through the sublattice restrictions

\[
\boxed{
 e_0\mid m,
\qquad
 d_0\mid m+j.
}
\tag{4}
\]

Thus the collective shift-position object is governed by one universal periodic kernel

\[
U_\chi(j,m):=\chi(m+j)\overline{\chi(m)}.
\tag{5}
\]

Moreover this kernel is not intrinsically two-dimensional. Under the invertible endpoint change of variables

\[
x=m+j,\qquad y=m,
\tag{6}
\]

one has

\[
\boxed{
U_\chi(j,m)=\chi(x)\overline{\chi(y)}.
}
\tag{7}
\]

So after the shift is promoted to a variable, the translated source phase becomes a tensor product. The nontrivial coupling has moved into the **domain geometry**: the divisor sublattices, interval endpoints, and the difference constraint `j=x-y`.

This separation is visible exactly in finite Fourier space. With

\[
\widehat U_\chi(r,s)
:=
\sum_{j,m\bmod q}
U_\chi(j,m)e_q(-rj-sm),
\qquad
e_q(t)=e^{2\pi i t/q},
\tag{8}
\]

the change `(6)` gives

\[
\widehat U_\chi(r,s)
=
\left(\sum_{x\bmod q}\chi(x)e_q(-rx)\right)
\left(\sum_{y\bmod q}\overline{\chi(y)}e_q((r-s)y)\right).
\tag{9}
\]

For primitive `chi`, the classical Gauss transform therefore implies

\[
\boxed{
\widehat U_\chi(r,s)=0
\quad\text{unless}\quad
(r,q)=(s-r,q)=1,
}
\tag{10}
\]

and on that support

\[
\boxed{
|\widehat U_\chi(r,s)|=q.
}
\tag{11}
\]

The two-dimensional spectrum is a flat unit-pair mask at amplitude `q`; it is not a generic square-root-sized two-variable Fourier object.

An elementary consequence is that for arbitrary sets `J,M` of residue classes modulo `q`, with `|J|=H` and `|M|=K`,

\[
\boxed{
\left|
\sum_{j\in J}\sum_{m\in M}
\chi(m+j)\overline{\chi(m)}
\right|
\le \sqrt{qHK}.
}
\tag{12}
\]

Hence plain orthogonality/Cauchy becomes nontrivial against the trivial bound `HK` only once `HK>q`. Ordinary two-dimensional Fourier completion gives the same qualitative conductor-area threshold, up to logarithms for interval cutoffs.

This is **not** a fundamental lower bound for the incomplete family. Bilinear multiplicative-character technology can beat generic Cauchy/completion in structured ranges, and the literature explicitly contains nontrivial estimates below the naive `UV\asymp p` area threshold. The correct negative conclusion is narrower:

> joint averaging over shift and position does not by itself create an additional source-character dimension. After an exact change of variables, the phase is endpoint-separable, and the first generic second-moment/completion bounds see only a flat Gauss spectrum. Any further gain must exploit the arithmetic geometry of the retained domain/weights or a genuinely stronger bilinear-character theorem, not merely the existence of the translated phase.

Equivalently, returning to the divisor-pair coordinates in `MC-413`, write

\[
n+h=dA,\qquad n=eB.
\tag{13}
\]

Then

\[
\boxed{
h=dA-eB,
\qquad
\chi(n+h)\overline{\chi(n)}
=
\chi(d)\overline{\chi(e)}\chi(A)\overline{\chi(B)}.
}
\tag{14}
\]

For a shift range `1\le h\le H`, the source phase is separable and all coupling sits in the thin diagonal strip

\[
1\le dA-eB\le H
\tag{15}
\]

plus the original endpoint cutoffs and well-factorable divisor coefficients. This identifies the actual next analytic object: a weighted bilinear character sum over divisor-dependent thin/convex domains, not an autonomous two-variable source phase.

No estimate for the Mertens function, no improved source-depth exponent, and no RH consequence follows.

## 1. The divisor-pair translation universalizes after removing the gcd

Start from the exact expansion in `MC-413`:

\[
C_h(N)
=
\sum_{d,e}\lambda_d\overline{\lambda_e}
\sum_{\substack{n\le N-h\\d\mid n+h\\e\mid n}}
\chi(n+h)\overline{\chi(n)}.
\tag{16}
\]

A pair contributes only when `g=(d,e)` divides `h`. Write `(2)` and `h=gj`. Since `e=ge_0` divides `n`, put `n=gm`. The simultaneous divisibilities become

\[
ge_0\mid gm,
\qquad
gd_0\mid g(m+j),
\tag{17}
\]

which are exactly `(4)`.

For the character phase, `MC-413` already proves that only `(de,q)=1` survives. In particular `(g,q)=1`, so complete multiplicativity gives

\[
\begin{aligned}
\chi(g(m+j))\overline{\chi(gm)}
&=\chi(g)\chi(m+j)\,
  \overline{\chi(g)}\overline{\chi(m)}\\
&=\chi(m+j)\overline{\chi(m)}.
\end{aligned}
\tag{18}
\]

This proves `(3)` exactly. The dependence on `(d,e)` has not vanished from the problem: it has moved entirely into the sampled sublattice and the archimedean range. What disappears is the claim that different divisor pairs carry genuinely different source-character phases once the shift itself is retained as a coordinate.

This does not contradict `MC-413`. There `h` is fixed, and after solving the two congruences the one-dimensional `k`-sum contains a genuine pair-dependent translation `h[d,e]^{-1}` modulo `q`. Here we ask a different collective question: what happens before fixing one `h`-slice? In that enlarged object, the invertible change `(n,h)=(gm,gj)` removes the divisor gcd from the source phase and places the remaining arithmetic dependence in the lattice on which the universal kernel is sampled.

## 2. Endpoint coordinates make the source phase a tensor product

Set `(x,y)=(m+j,m)`. This is an invertible linear transformation of `(j,m)` modulo `q`, with inverse

\[
j=x-y,\qquad m=y.
\tag{19}
\]

Equation `(7)` follows immediately. A second useful form is obtained when `m` is a unit modulo `q`:

\[
U_\chi(j,m)
=
\chi\!\left(1+jm^{-1}\right).
\tag{20}
\]

Thus the same kernel can be viewed either as a product of endpoint characters or as a projective one-variable character of the slope `j/m`. In particular, for every unit `t mod q`,

\[
U_\chi(tj,tm)=U_\chi(j,m).
\tag{21}
\]

The two-dimensional appearance therefore contains a scaling redundancy. A successful bilinear estimate may exploit the way the actual divisor/interval domain cuts across these projective or endpoint coordinates, but the kernel itself does not supply two independent source phases.

The endpoint form also explains `(14)` directly. Set `A=(n+h)/d` and `B=n/e`; then `h=dA-eB`. On the surviving coprime-to-`q` divisor pairs,

\[
\chi(dA)\overline{\chi(eB)}
=
\chi(d)\overline{\chi(e)}
\chi(A)\overline{\chi(B)}.
\tag{22}
\]

The prefactor `chi(d)overline{chi(e)}` depends on the outer divisor pair but the inner oscillation is separable. Any genuine gain from summing over many shifts must therefore come from the geometry of the strip `(15)`, cancellation in the divisor coefficients, or a theorem that uses both together.

## 3. Exact two-dimensional Gauss spectrum and the generic second-moment bound

Equation `(9)` is just the endpoint factorization in Fourier coordinates. For a primitive Dirichlet character modulo `q`, the classical Gauss-sum identity says

\[
\left|\sum_{x\bmod q}\chi(x)e_q(ax)\right|
=
\begin{cases}
\sqrt q,&(a,q)=1,\\
0,&(a,q)>1.
\end{cases}
\tag{23}
\]

Applying `(23)` separately to the two factors in `(9)` proves `(10)`--`(11)`.

Now let

\[
S(J,M)=
\sum_{m\in M}\overline{\chi(m)}
\sum_{j\in J}\chi(m+j).
\tag{24}
\]

Cauchy gives

\[
|S(J,M)|^2
\le
K\sum_{m\bmod q}
\left|\sum_{j\in J}\chi(m+j)\right|^2.
\tag{25}
\]

By finite Fourier Parseval and `(23)`,

\[
\sum_{m\bmod q}
\left|\sum_{j\in J}\chi(m+j)\right|^2
=
\sum_{\substack{r\bmod q\\(r,q)=1}}
|\widehat{1_J}(r)|^2
\le qH.
\tag{26}
\]

This proves `(12)`.

For interval indicators, applying `(9)` directly and using the standard `ell^1` Fourier norm `O(q log q)` for an interval gives a generic completed estimate on the order of `q log^2 q` (with harmless convention-dependent absolute constants). Neither `(12)` nor this completed bound uses the well-factorable divisor structure. They are useful as **baseline obstructions**: if a proposed collective argument only performs ordinary Cauchy, Parseval, or completion on the universal kernel, it has not yet used the information that distinguishes the `MC-409` representation from a generic shifted character family.

The threshold `HK>q` from `(12)` must not be promoted to a universal barrier. It is only the threshold of this elementary second-moment route.

## 4. Prior art shows that the domain geometry can matter below the generic threshold

The relevant classical/modern literature prevents a stronger no-go claim.

Karatsuba developed double multiplicative-character estimates for genuinely additive two-variable configurations, and later work obtains nontrivial bounds in parameter ranges where a direct `sqrt(UVp)` estimate is still trivial. A useful modern reference is Igor E. Shparlinski, *On Bilinear Exponential and Character Sums with Reciprocals of Polynomials*, Mathematika **62** (2016), 842--859, DOI `10.1112/S0025579316000036`, arXiv:`1504.03192`.

Shparlinski studies weighted bilinear multiplicative-character sums over convex domains and explicitly records the generic benchmark

\[
O(\sqrt{UVp}\log p),
\tag{27}
\]

while developing stronger estimates that can be nontrivial when `UV` is much smaller than `p`. In the multiplicative-character section he notes that the degree-one case has stronger Karatsuba bounds, while his Theorem 2.6 handles higher-degree polynomial shifts in additional ranges. The same paper rewrites its character sums in reciprocal form, making it structurally adjacent to `(20)`.

This literature is a **prior-art boundary, not a theorem transplant**. The current Mathia object has several extra layers absent from a bare rectangle: the outer well-factorable divisor pair, the compatibility `(d,e)|h`, divisor-dependent sublattices, a thin difference strip such as `(15)`, source conductors that need not be prime, and the downstream source-depth/common-radical accounting. None of the cited bilinear estimates automatically controls that full object or yields the saving required by the prime-frame argument.

The exact contribution of this finding is therefore representational: it identifies where any such theorem would have to act. The character kernel itself re-separates under collective shift-position coordinates; the remaining potentially useful information is the structured **sampling geometry and coefficient family**.

## Boundaries and falsification tests

- **No contradiction with `MC-413`.** For a fixed `h`, the incomplete translated sum remains genuinely nonseparable in its one-dimensional progression coordinate. The present result classifies the enlarged object in which `h` is also summed or averaged.
- **The divisor pair is not erased from the full sum.** Equations `(4)`, `(14)`, and `(15)` retain divisor-dependent lattices, strip slopes, endpoints, block lengths, and coefficient weights. Only the source-character kernel universalizes/separates.
- **The flat Fourier spectrum is not a no-go for deeper bilinear methods.** Karatsuba/Shparlinski-type estimates can exploit structure beyond one Cauchy/Parseval step. Any claim that `HK\le q` makes cancellation impossible would be false.
- **Primitive conductor is load-bearing for `(10)`--`(11)`.** An imprimitive presentation must first descend to its primitive conductor. The gcd reduction `(3)` uses the same `(de,q)=1` surviving regime already established in `MC-413`.
- **Projective reduction does not make the sampled domain one-dimensional.** The kernel depends on a slope, but the arithmetic lattice and archimedean strip need not be invariant under scaling. Counting or estimating those fibers remains a genuine problem.
- **Generic bilinear theorems do not automatically survive the outer sieve sum.** A usable transfer must keep the actual `lambda_d overline{lambda_e}` or well-factorable decomposition, verify the theorem's support/modulus hypotheses, and propagate every conductor, exceptional-set, common-radical, and source-depth cost.
- **No RH-scale statistic is imported.** The derivation uses only finite divisor algebra, complete multiplicativity, and finite Gauss/Fourier identities. No continuation of `1/zeta`, zero-free region, or Mertens estimate is used.

## Consequence for the research line

`MC-413` correctly located all fixed-shift divisor-dependent character information in incomplete conductor blocks. The present result narrows the accepted retained-variable clue one step further: **simply averaging those blocks over the differencing shift does not preserve a new mixed source phase**. Once shift and position are treated jointly, the source kernel becomes the endpoint tensor product `chi(x)overline{chi(y)}`, with a flat primitive Gauss spectrum.

The next decisive test should therefore be geometric/analytic rather than representational. For a concrete well-factorable component, retain the exact outer divisor weights and rewrite the joint incomplete contribution in endpoint variables `(A,B)` with its strip `1<=dA-eB<=H`. Determine whether a Karatsuba/Shparlinski-type bilinear character estimate, a dispersion theorem, or a modulus-factorization argument genuinely applies to that **weighted thin-domain family** in a range that survives the later source-frame bookkeeping.

If the analysis reduces only to `(12)`, ordinary completion, or separate one-dimensional character bounds, the route has returned to a generic conductor-area/source-cost barrier. If a stronger theorem uses the divisor-factorable strip geometry and yields a strict post-summation gain, that is the remaining place where the `MC-409` representation can still alter the source-depth frontier.
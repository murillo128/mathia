# RE-186 — Microstepped Chebyshev repair reaches every subcritical scalar jet depth

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + SUBCRITICAL-EULER-JET-MATCHING + MICROSTEPPED-SHELL-PACKING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-185-STRENGTHENING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-178, RE-184, RE-185.

`RE-185` removes the monomial-conditioning loss from `RE-184` and matches all Euler boundary jets through every depth `K=o(V(p))`, and even through a sufficiently small constant fraction of

\[
V(p):=\frac{(\log p)^{3/5}}{(\log\log p)^{1/5}}.
\]

Its remaining exponential cost `e^{O(K)}` comes from moving each repair generation by a whole normalized interpolation window before recentering the Chebyshev basis. That transport cost is not forced by ordinary-prime quantization. One can move the repair baseline in exponentially smaller logarithmic microsteps while assigning the `K+1` shell tracks distinct residues modulo the microstep. The shell supports then remain globally disjoint, but the inter-generation Chebyshev translation becomes only polynomially conditioned.

This closes the entire asymptotic gap below the scalar capacity crossover of `RE-178`.

Let `K=K(p)` be integer valued and satisfy

\[
\boxed{
K(p)\log\log p=o(\log p).
}
\tag{1}
\]

Equivalently,

\[
K(p)=o\!\left(\frac{\log p}{\log\log p}\right).
\]

For every sufficiently large selector prime `p`, there exists an ordinary-prime-supported source `Q_{p,K}` with

\[
\boxed{m_{Q_{p,K}}(q)\in\{0,1,2\}}
\tag{2}
\]

such that, writing

\[
D_Q(s):=\sum_q(m_Q(q)-1)[-\log(1-q^{-s})],
\]

all of the following hold:

1. `Q_{p,K}` agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p\subset[2p,3p]` and has no repair below `16p`;
3. every Euler boundary derivative through depth `K` matches exactly,
   \[
   \boxed{D_{Q_{p,K}}^{(j)}(1+)=0,\qquad 0\le j\le K;}
   \tag{3}
   \]
4. the correction series is absolutely convergent in every derivative in (3), so termwise differentiation is legitimate;
5. uniformly for `X\ge2p`,
   \[
   \boxed{
   |\vartheta_{Q_{p,K}}(X)-\vartheta(X)|
   \le
   p^{1/2+o(1)}+p^{o(1)}(1+\log X)^2,
   }
   \tag{4}
   \]
   where the `o(1)` is along the family (1); consequently every fixed Korobov--Vinogradov envelope
   \[
   |\vartheta_{Q_{p,K}}(X)-\vartheta(X)|\ll_b X e^{-bV(X)}
   \tag{5}
   \]
   holds for all sufficiently large `p`;
6. before repair is visible, the normalized Robin coordinate retains the canonical order-one excursion,
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_{p,K})-
   \mathcal A_{p,8p}(P)\asymp1.
   }
   \tag{6}
   \]

Thus every boundary-jet depth strictly below

\[
K_{\rm cap}(p)\asymp\frac{\log p}{\log\log p}
\]

remains exactly non-rigid in the same honest ordinary-prime `{0,1,2}` source class. The `Theta(V(p))` boundary of `RE-185` was therefore still architectural: it came from coarse inter-generation transport, not from the prime-shell resolution itself.

## 1. Fixed-width Chebyshev coordinates isolate the real large-order error

Retain the exact Euler kernels

\[
H(q):=\log\frac q{q-1},
\qquad
U_j(q):=(\log q)^j\sum_{m\ge1}m^{j-1}q^{-m}
\quad(j\ge1),
\]

with `U_0=H`, and the exact centered kernels at baseline `x=e^L`,

\[
C_{j,L}(q)
:=
\sum_{r=0}^j\binom jr(-L)^{j-r}U_r(q).
\tag{7}
\]

Fix once and for all a logarithmic interpolation width `W=1`. Define

\[
P_m(\alpha):=T_m(2\alpha-1),
\qquad 0\le\alpha\le1,
\tag{8}
\]

and write `P_m(t)=\sum_{j=0}^m a_{mj}t^j`. The exact moving coordinates are

\[
\Psi_{m,L}(q)
:=
\sum_{j=0}^m a_{mj}C_{j,L}(q),
\qquad 0\le m\le K.
\tag{9}
\]

For each fixed `L`, the change of basis in (9) is triangular with nonzero diagonal. Vanishing of all `\Psi_{m,L}` through degree `K` is therefore exactly equivalent to vanishing of the raw Euler jets `U_0,\ldots,U_K`.

The `n=1` Euler-factor term gives exactly the polynomial response `P_m(\alpha)`, where `\alpha=\log(q/x)`. The prime-power terms are the only analytic error. The elementary estimate used in `RE-184` gives

\[
\frac{C_{j,L}(q)}{H(q)}
=
\alpha^j+
O\!\left(
\frac{2^K(2L+2)^j}{x}
\right)
\tag{10}
\]

uniformly for `j\le K`, `0\le\alpha\le1`, and every later baseline. Since the coefficients of `T_m(2t-1)` have total weighted size at most `C^m` after a fixed-width rescaling, (10) yields

\[
\boxed{
\frac{\Psi_{m,L}(q)}{H(q)}
=P_m(\alpha)+\mathcal E_{m,L}(q),
\qquad
\max_{m\le K}|\mathcal E_{m,L}(q)|
\le
\exp\{-L+O(K\log(L+2))\}.
}
\tag{11}
\]

Condition (1) is exactly what makes the error in (11) negligible already at `L\asymp\log p`:

\[
K\log L=o(L).
\tag{12}
\]

Unlike `RE-185`, no `V(p)` restriction appears in this analytic step. The natural large-order boundary of the exact Euler-factor approximation is the same subcritical scale identified independently by the raw capacity calculation in `RE-178`.

## 2. Pack infinitely many repair generations into disjoint microstep tracks

Let `a_0>0` be fixed so that the line's anchored unconditional PNT implies

\[
\vartheta(y)=y+O\bigl(y e^{-a_0V(y)}\bigr).
\tag{13}
\]

Set

\[
h:=e^{-a_0V(p)/8},
\qquad
x_n:=16p\,e^{nh},
\qquad n\ge0,
\tag{14}
\]

and give generation `n` shell width

\[
\delta_n:=e^{-a_0V(x_n)/4}.
\tag{15}
\]

The crucial point is that the repair baseline now advances by only `h` in logarithmic coordinates, rather than by `Theta(K)` as in `RE-185`.

Start from the Gauss--Chebyshev nodes

\[
\bar\alpha_r
:=
\frac12\left(1+\cos\frac{(2r+1)\pi}{2(K+1)}\right),
\qquad 0\le r\le K.
\tag{16}
\]

Their smallest spacing and distance from the endpoints are `\asymp K^{-2}`. Since `h` is smaller than every negative power of `K` under (1), we may choose perturbed nodes `\alpha_r\in(0,1)` such that

\[
|\alpha_r-\bar\alpha_r|\le h,
\qquad
\boxed{
\alpha_r\equiv\frac{rh}{K+1}\pmod h.
}
\tag{17}
\]

At generation `n`, put the `r`-th prime shell around

\[
y_{n,r}:=x_ne^{\alpha_r}.
\tag{18}
\]

The residue assignment in (17) makes the shell centers globally separated, not merely separated inside one generation. For two distinct pairs `(n,r)\ne(m,s)`,

\[
\begin{aligned}
|\log y_{n,r}-\log y_{m,s}|
&=
\left|
\left(n-m+k_r-k_s+\frac{r-s}{K+1}\right)h
\right|\\
&\ge \frac{h}{K+1},
\end{aligned}
\tag{19}
\]

where the integers `k_r` come from (17). On the other hand,

\[
\delta_n\le e^{-a_0V(p)/4}=h^2=o(h/K).
\tag{20}
\]

Hence all prime shells from all generations are pairwise disjoint once `p` is large. There is no prime reuse and no hidden multiplicity growth.

Subtracting (13) at the endpoints of each shell gives, uniformly in `n,r`,

\[
\boxed{
\sum_{q\in I_{n,r}}H(q)
\asymp\frac{\delta_n}{\log x_n}.
}
\tag{21}
\]

The PNT supply therefore remains far larger than any requested repair mass below.

## 3. The shell matrix stays DCT-conditioned far beyond the KV depth

At the ideal nodes (16), the limiting response matrix is

\[
A_K(m,r)=P_m(\bar\alpha_r)
=\cos\frac{m(2r+1)\pi}{2(K+1)}.
\tag{22}
\]

Discrete cosine orthogonality gives the explicit inverse used in `RE-185` and, in particular,

\[
\boxed{
\|A_K^{-1}\|_{\infty\to1}\ll K.
}
\tag{23}
\]

The perturbation (17) changes each entry by at most `O(K^2h)` because `|T_m'|\le m^2` on `[-1,1]`. Across an actual prime shell, the additional variation is `O(K^2\delta_n)`. Finally, (11) contributes the exact Euler-factor error. Hence the exact shell response matrix `A_n` satisfies

\[
\|A_n-A_K\|_{1\to\infty}
\ll
K^2(h+\delta_n)
+
\exp\{-L_n+O(K\log(L_n+2))\},
\tag{24}
\]

where `L_n=\log x_n`. Combining (23), (24), `Kh=o(1)`, and (12), a Neumann perturbation yields

\[
\boxed{
\|A_n^{-1}\|_{\infty\to1}\ll K
}
\tag{25}
\]

uniformly in every generation.

This is the first important separation from `RE-185`: the PNT shell width still decays on the KV scale, but the number of interpolated scalar coordinates may grow all the way through (1). The shell matrix does not itself force `K=O(V(p))`.

## 4. Microstep recentering costs only polynomially

Move from baseline `L` to `L+h`. Since the coordinates (9) are exact polynomial combinations of the same raw Euler kernels, recentering is exact algebra. In normalized variable `z=2\alpha-1`, it is just

\[
z\mapsto z-2h.
\tag{26}
\]

For `|z|\le1`,

\[
|T_m(z-2h)|
\le
\exp\{C m\sqrt h\}.
\tag{27}
\]

Indeed, outside `[-1,1]` the extremal value is controlled by `T_m(1+2h)=\cosh(m\operatorname{arcosh}(1+2h))`, and `\operatorname{arcosh}(1+2h)=O(\sqrt h)`. Expanding `T_m(z-2h)` back into the Chebyshev basis, the standard coefficient formula therefore gives a row-sum bound

\[
\boxed{
\|\mathcal T_h\|_{\infty\to\infty}
\ll
K\,e^{CK\sqrt h}.
}
\tag{28}
\]

Under (1),

\[
K\sqrt h
=K e^{-a_0V(p)/16}=o(1),
\tag{29}
\]

so the exact inter-generation transport costs only `O(K)`. The `e^{CK}` recentering factor in `RE-185` has disappeared without weakening ordinary-prime support or integer multiplicity.

This is not a better polynomial basis for a coarse generation jump. It is a different repair geometry: **move the source reservoir in microsteps, and use congruence-separated shell tracks to keep every generation disjoint**.

## 5. Quantization contracts despite the enormous number of generations

Let `M_n` be the `\ell^\infty` norm of the exact `K+1`-coordinate residual at baseline `L_n`. Solve the real shell system using (25), then quantize as in `RE-184`--`RE-185`: in each shell select distinct ordinary primes until the required signed `H`-mass is reached from below. Positive mass duplicates one ordinary copy and negative mass deletes one copy. Because of global disjointness, every prime is touched at most once, so (2) is automatic.

The inverse bound gives total requested signed mass `O(KM_n)`. Shell variation and one-prime rounding give, at the same baseline,

\[
M_n'
\le
\eta_n M_n+
O\!\left(\frac K{x_n}\right),
\tag{30}
\]

where

\[
\eta_n
\ll
K^3\delta_n
+
K\exp\{-L_n+O(K\log(L_n+2))\}.
\tag{31}
\]

After exact recentering by (28),

\[
M_{n+1}
\le
O(K)\eta_nM_n+
O\!\left(\frac{K^2}{x_n}\right).
\tag{32}
\]

Because `\delta_n\le h^2=e^{-a_0V(p)/4}` and (12) holds uniformly at every later baseline, for sufficiently large `p`

\[
O(K)\eta_n\le\frac13
\qquad(n\ge0).
\tag{33}
\]

The initial deletion packet is below the repair window. At `x_0=16p`, its normalized Chebyshev argument lies in one fixed compact interval outside `[-1,1]`, so

\[
\boxed{
M_0\le C_0^K d_p,
\qquad
d_p\asymp\frac1{\sqrt p\log p}.
}
\tag{34}
\]

Condition (1) implies `C_0^K=p^{o(1)}`. The first-generation requested mass is therefore `p^{-1/2+o(1)}`, whereas the available shell mass (21) is only subpolynomially small. Every later target is still smaller.

Iterating (32)--(33) gives

\[
M_n
\ll
3^{-n}M_0
+
K^2\sum_{r<n}\frac{3^{-(n-1-r)}}{x_r},
\tag{35}
\]

and in particular `M_n\to0`.

The fact that `h` is tiny creates about `h^{-1}` generations per unit increase of `\log x`, but

\[
h^{-1}=e^{a_0V(p)/8}=p^{o(1)}.
\tag{36}
\]

Thus the enormous generation count is still only subpolynomial at the selector scale. It does not undo the gain from microstepping.

## 6. Exact matching and absolute convergence survive the microstep limit

For fixed `p`, the integer `K=K(p)` is finite. The total signed `H`-mass in generation `n` is `O(KM_n)`. For every raw derivative order `0\le j\le K`, its absolute contribution is therefore bounded by

\[
O\bigl(KM_n(L_n+2)^j\bigr).
\tag{37}
\]

The geometric part of (35) is summable against every fixed power of `L_n`, while the rounding floor is controlled by

\[
\sum_{n\ge0}\frac{(L_0+nh+2)^j}{x_0e^{nh}}
<\infty.
\tag{38}
\]

Hence the full correction is absolutely convergent in all derivatives through order `K`.

Moreover, conversion from the moving Chebyshev coordinates back to any raw jet costs only a polynomial in `L_n` of degree at most `K`. Since `M_n` has a geometric part plus an `x_n^{-1}` floor, that converted residual tends to zero. Taking the limit of the finite-stage exact identities therefore gives (3).

This point matters: the proof does not infer exactness from an asymptotic formal series. It constructs a sequence of honest finite ordinary-prime edits, proves absolute convergence of the relevant Euler derivatives, and drives the exact residual vector to zero.

## 7. Source fidelity survives the denser repair schedule

The first correction cluster uses `p^{1/2+o(1)}` ordinary primes in total, including the canonical selector packet and the geometrically decaying early repairs. Its total Chebyshev discrepancy is therefore `p^{1/2+o(1)}`.

Once the one-prime rounding floor dominates, each generation edits only `K^{O(1)}` primes. Up to a cutoff `X`, there are at most

\[
O\!\left(1+\frac{\log(X/p)}h\right)
\tag{39}
\]

microstep generations. Since every edited prime contributes `O(\log X)` to `\vartheta`, (34)--(36) give

\[
|\vartheta_Q(X)-\vartheta(X)|
\ll
p^{1/2+o(1)}
+
K^{O(1)}h^{-1}(1+\log X)^2.
\tag{40}
\]

Under (1), both `K^{O(1)}` and `h^{-1}` are `p^{o(1)}`, yielding (4).

For each fixed `b>0`, the right side of (4) is `o(p e^{-bV(p)})` at the selector scale, and `X e^{-bV(X)}` is eventually increasing. This proves the fixed KV fidelity (5) uniformly for `X\ge2p`.

Finally, all repair shells begin at `16p`. The canonical deletion packet is unchanged below the transient cutoff `8p`, so the order-one Robin excursion (6) is exactly the same one already established in `RE-173`--`RE-185`.

## 8. What actually moved the boundary

`RE-185` correctly showed that monomial conditioning was not intrinsic, but its generations still jumped by one whole normalized shell window. Translating a degree-`K` Chebyshev basis by a fixed normalized distance costs `e^{Theta(K)}`, which naturally meets the PNT shell error at `K=Theta(V(p))`.

The present construction separates two scales that were previously tied together:

\[
\text{prime-shell width }\delta\asymp e^{-cV(p)}
\qquad\text{and}\qquad
\text{generation step }h\asymp e^{-cV(p)/2}.
\tag{41}
\]

Because `\delta\ll h/K`, residues modulo `h` keep all shell tracks disjoint. Because `K\sqrt h=o(1)`, the moving polynomial frame is only polynomially distorted from one generation to the next. Because `h^{-1}=p^{o(1)}`, paying for many more generations does not threaten source fidelity.

The surviving restriction is no longer `K=O(V(p))`. It comes from the **prime-power part of the exact Euler kernel** in (11): a degree-`K` exact boundary coordinate carries an error of size roughly

\[
\exp\{-\log p+O(K\log\log p)\}.
\tag{42}
\]

That is precisely why the proof stops at (1), the same scale at which `RE-178` says raw scalar jet leverage first becomes polynomially visible.

## 9. Representation audit

The generic machinery is approximation theory and elementary packing: fixed-width Chebyshev interpolation, discrete cosine orthogonality, a small-translation bound for Chebyshev polynomials, and assigning finitely many tracks distinct residues modulo a microstep. None of those ingredients is specific to primes or Robin's inequality.

The source-specific content is the coupling of that machinery to four arithmetic constraints simultaneously: the exact Euler-factor kernels, ordinary-prime reservoirs supplied by the KV PNT in exponentially thin relative shells, one-copy deletion/duplication so multiplicities stay in `{0,1,2}`, and preservation of the canonical pre-repair Robin excursion. The argument transfers to other moment-matching problems only when an analogous source supplies infinitely many disjoint quantization reservoirs with atom size tending to zero.

The limitation is equally important. This is still a **matched-control non-rigidity theorem**. It does not say that Robin's original source naturally supplies the matched jets, and it does not weaken the exact identification theorem `RE-174` for the full Euler germ. It says that every asymptotically subcritical finite truncation of that germ remains insufficient, even after restoring ordinary-prime support and bounded nonnegative integer multiplicity.

## 10. Adversarial self-review

The main possible failure is shell reuse. Equation (19) rules it out globally: the tracks have distinct residues modulo `h`, and the PNT shell width is `o(h/K)`. The construction therefore never asks one ordinary prime to be deleted and duplicated at different stages.

A second possible failure is that taking exponentially many microsteps could accumulate a macroscopic source discrepancy. Equation (36) is the relevant accounting: only `e^{O(V(p))}=p^{o(1)}` generations occur per unit logarithmic distance, while after the initial correction cluster each generation changes only polynomially many primes. This gives (40), not an uncontrolled sum of shell capacities.

A third possible failure is hidden conditioning in the moving frame. The large fixed translation from `RE-185` would indeed reintroduce `e^{Theta(K)}`. Here the translation distance is `2h`, and (27)--(29) bound the exact Chebyshev basis change before any asymptotic Euler approximation is made. The gain is therefore geometric, not a cancellation assumption.

A fourth possible failure is the exact Euler-factor remainder. This is the true new bottleneck. The fixed-width Chebyshev basis costs only `C^K`, but the centered raw kernels still carry `(\log p)^K` against the `q^{-2}` prime-power tail. Condition (1) is precisely what keeps that error `p^{-1+o(1)}`. No claim is made at `K\asymp\log p/\log\log p` with an arbitrary fixed leading constant.

Finally, the theorem does not establish source rigidity at the crossover. It merely removes the entire `o(K_cap)` region from consideration. At the critical scale one must either control the exact prime-power response without the `e^{K\log\log p}` loss, or exploit genuinely joint/integral information that cannot be implemented by shellwise scalar interpolation.

## 11. Prior-art audit

The approximation ingredients are classical: Chebyshev nodes, the discrete cosine transform, Markov's derivative bound, and the elementary growth formula `T_m(\cosh u)=\cosh(mu)`. The prime supply is exactly the Korobov--Vinogradov PNT input already anchored in `SOURCES.md`; Bellotti's current zero-density/PNT work remains the line's external source for that scale.

A broad targeted search found the expected literature on Chebyshev transforms, shifted polynomial interpolation, Beurling/generalized Euler products, and modern KV-type PNT error terms, but no theorem matching the source-specific construction here: infinitely many globally disjoint microstepped ordinary-prime shells, `{0,1,2}` quantization, exact matching of a growing Euler-jet stack, fixed KV fidelity, and a preserved transient Robin excursion. No new external theorem is load-bearing, so `SOURCES.md` needs no change.

## Conclusion

The `Theta(V(p))` limit in `RE-185` was not an ordinary-prime information barrier. It came from translating the interpolation frame by an entire window after each quantization step. Microstepping the baseline and separating shell tracks by residues modulo the microstep removes that exponential transport cost while keeping every prime support disjoint.

As a result, exact source-faithful matched non-rigidity now holds for every

\[
K=o\!\left(\frac{\log p}{\log\log p}\right),
\]

which is the whole asymptotically subcritical range below the scalar capacity crossover of `RE-178`. The live scalar frontier has moved to the crossover itself.
# RE-162 — Chebyshev interpolation pins the growing-moment terminal threshold at four factorial radii

**Status:** `EXACT-DERIVED + SHARP-GROWING-MOMENT-CAPACITY + CHEBYSHEV-INTERPOLATION-UPPER + CHEBYSHEV-LEVEL-SET-LOWER + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-157, RE-159, RE-160, RE-161.

`RE-160` identified the growing-order terminal scale

\[
\tau_r(p):=\bigl(r!\,\eta_p\bigr)^{1/r},
\qquad
\eta_p:=\frac{\log U_A(p)}{\sqrt p\log p},
\]

and showed that the transition for exact matching of the first `r-1` terminal placement moments lies at

\[
L\asymp r\,\eta_p^{1/r}.
\]

Its upper bound came from Taylor expansion at one endpoint, while its lower construction used Prouhet--Thue--Morse packets. Those two devices locate the correct order but leave a large universal-constant gap. The gap is not intrinsic. Once the moment constraints are treated as a polynomial-approximation problem, the exact terminal kernel has an asymptotically sharp Chebyshev capacity.

Let

\[
U:=U_A(p),
\qquad
G_U(z)
:=U\left[a(Ue^{-z})-a(U)+\frac{a(U)}{\log U}z\right],
\qquad
a(t):=-\log(1-t^{-1}),
\]

as in `RE-160`--`RE-161`. Let `r=r(p)>=2`, let `L=L_p=o(1)`, and suppose

\[
\rho_{r,U,L}:=\frac{2^{r-1}e^L}{U}=o(1).
\]

For two equal-cardinality packets with empirical probability measures `mu_1,mu_2` on `[0,L]`, assume exact moment matching

\[
\int z^k\,d\mu_1(z)=\int z^k\,d\mu_2(z)
\qquad (0\le k<r).
\]

Define the normalized terminal-kernel capacity

\[
D_{r,U}(L)
:=
\sup_{\mu_1,\mu_2}
\left|
\int G_U(z)\,d(\mu_1-\mu_2)(z)
\right|.
\]

Then

\[
\boxed{
D_{r,U}(L)
=
(4+o(1))\frac{(L/4)^r}{r!}.
}
\tag{1}
\]

The upper bound holds for arbitrary equal-cardinality packets. The lower bound is realized asymptotically by two `r`-point packets obtained as opposite level sets of a scaled monic Chebyshev polynomial, and these blocks can be translated generically and repeated while keeping all inserted labels distinct.

Consequently, if

\[
m_p\sim\delta_p\frac{U}{\log U},
\qquad
\delta_p\to0,
\]

and `m_p/r -> infinity`, the maximal normalized Robin-source separation among exact `r-1` moment-matched insertion packets is

\[
\boxed{
\operatorname{Cap}^{(r)}_p(L,\delta)
=
(2+o(1))\,\delta_p
\left(\frac{L}{4\tau_r(p)}\right)^r.
}
\tag{2}
\]

Thus the vanishing-budget transition is not merely known up to universal constants. Put

\[
F_p:=\left(\frac{L}{4\tau_r(p)}\right)^r.
\]

If `F_p=O(1)`, every family with `delta_p -> 0` has `o(1)` Robin-source leverage. If `F_p -> infinity`, then, in the same growing-order regime and with `r log U/U -> 0`, there exist PNT-small exact moment-matched controls with `delta_p -> 0` and any prescribed fixed source separation. Equivalently, the sharp factorial radius is

\[
\boxed{
L_{\mathrm{crit}}
=4\tau_r(p)
=\left(\frac4e+o(1)\right)
r\,\eta_p^{1/r}.
}
\tag{3}
\]

This sharpens `RE-160`: its order-of-magnitude phase law remains correct, but both the stability and obstruction sides meet at the same Chebyshev constant `4`.

## 1. Exact moment matching turns the problem into polynomial approximation

The insertion influence from `RE-160` is

\[
\Lambda_p(Ue^{-z})
=
\frac{\sqrt p\log p}{Z_pU}\,G_U(z),
\qquad
Z_p=2+o(1).
\tag{4}
\]

For two packets of `m` labels with empirical measures `mu_1,mu_2`, their normalized Robin-source difference is therefore

\[
\Delta\mathcal A_p
=
-\frac{m\sqrt p\log p}{Z_pU}
\int G_U\,d(\mu_1-\mu_2).
\tag{5}
\]

If the moments through degree `r-1` agree, then every polynomial `P` of degree at most `r-1` disappears from the signed integral:

\[
\int P\,d(\mu_1-\mu_2)=0.
\tag{6}
\]

Hence for any such `P`,

\[
\left|
\int G_U\,d(\mu_1-\mu_2)
\right|
\le
2\|G_U-P\|_{L^\infty([0,L])}.
\tag{7}
\]

The factor `2` is only the total variation of the difference of two probability measures. This replaces the endpoint Taylor remainder used in `RE-160` by a global degree-`r-1` approximation problem on the whole terminal interval.

## 2. Chebyshev interpolation gains the missing factor `4^{-r}`

Let `C_{r,L}` be the monic Chebyshev polynomial on `[0,L]`,

\[
C_{r,L}(z)
:=
\frac{L^r}{2^{2r-1}}
T_r\!\left(\frac{2z}{L}-1\right).
\tag{8}
\]

Its `r` roots lie in `(0,L)` and

\[
\boxed{
\|C_{r,L}\|_\infty
=
2\left(\frac L4\right)^r.
}
\tag{9}
\]

Interpolate `G_U` at those `r` roots by a polynomial `P_{r-1}` of degree at most `r-1`. The Lagrange remainder gives, pointwise on `[0,L]`,

\[
G_U(z)-P_{r-1}(z)
=
\frac{G_U^{(r)}(\xi_z)}{r!}\,C_{r,L}(z)
\]

for some `xi_z in (0,L)`. For `r>=2`, differentiating the absolutely convergent exact series yields

\[
G_U^{(r)}(z)
=
U\sum_{n\ge1}
\frac{n^{r-1}e^{nz}}{U^n}.
\tag{10}
\]

The `n=1` term gives the useful lower bound

\[
G_U^{(r)}(z)\ge e^z\ge1.
\tag{11}
\]

For the upper bound, `n<=2^{n-1}` implies

\[
G_U^{(r)}(z)
\le
 e^L
\sum_{n\ge1}
\left(
\frac{2^{r-1}e^L}{U}
\right)^{n-1}
=
\frac{e^L}{1-\rho_{r,U,L}}.
\tag{12}
\]

Combining (7), (9), and (12),

\[
\boxed{
D_{r,U}(L)
\le
\frac{4e^L}{1-\rho_{r,U,L}}
\frac{(L/4)^r}{r!}.
}
\tag{13}
\]

When `L=o(1)` and `rho_{r,U,L}=o(1)`, this is

\[
D_{r,U}(L)
\le
(4+o(1))\frac{(L/4)^r}{r!}.
\tag{14}
\]

The improvement over the endpoint Taylor bound is exponential in `r`: exact lower-moment matching lets the approximating polynomial oscillate across the whole interval, and the monic degree-`r` error envelope has Chebyshev norm `2(L/4)^r` rather than endpoint size `L^r`.

## 3. Opposite Chebyshev level sets attain the same constant

The upper bound is asymptotically sharp inside the same equal-weight packet class. Let `I=[s,s+W]` be any interval strictly inside `[0,L]`, and let

\[
C_{r,I}(z)
=
2\left(\frac W4\right)^r
T_r\!\left(\frac{2(z-s)}W-1\right)
\tag{15}
\]

be its monic Chebyshev polynomial. Write

\[
A_{r,W}:=2\left(\frac W4\right)^r.
\tag{16}
\]

Fix `0<a<1`. The equations

\[
C_{r,I}(z)=aA_{r,W},
\qquad
C_{r,I}(z)=-aA_{r,W}
\tag{17}
\]

each have exactly `r` distinct roots in the interior of `I`. Call the two root sets `Z_a` and `Y_a`.

The monic polynomials with these roots are

\[
C_{r,I}(z)-aA_{r,W},
\qquad
C_{r,I}(z)+aA_{r,W}.
\]

They differ only in their constant term. Newton's identities therefore give

\[
\boxed{
\sum_{z\in Z_a}z^k
=
\sum_{y\in Y_a}y^k
\qquad(1\le k<r).
}
\tag{18}
\]

Thus a block uses only `r` labels per packet, rather than the `2^{r-1}` labels of the Prouhet--Thue--Morse block used in `RE-160`.

To evaluate its full nonlinear kernel response, not merely the first uncancelled Taylor coefficient, let `x_1(c),...,x_r(c)` be the roots of

\[
C_{r,I}(x)=c,
\qquad |c|<A_{r,W},
\]

and define

\[
S(c):=\sum_{j=1}^rG_U(x_j(c)).
\tag{19}
\]

Implicit differentiation gives

\[
S'(c)
=
\sum_{j=1}^r
\frac{G_U'(x_j(c))}{C_{r,I}'(x_j(c))}.
\tag{20}
\]

Because `C_{r,I}(z)-c` is monic, the right-hand side is exactly the divided difference

\[
G_U'[x_1(c),...,x_r(c)].
\]

The divided-difference mean-value theorem therefore gives a point `xi_c in I` such that

\[
S'(c)
=
\frac{G_U^{(r)}(\xi_c)}{(r-1)!}.
\tag{21}
\]

Using (11),

\[
S'(c)\ge\frac1{(r-1)!}.
\]

Integrating from `-aA_{r,W}` to `aA_{r,W}` yields

\[
S(aA_{r,W})-S(-aA_{r,W})
\ge
\frac{2aA_{r,W}}{(r-1)!}.
\tag{22}
\]

After dividing by the `r` atoms in each packet,

\[
\boxed{
\left|
\int G_U\,d(\mu_{Z_a}-\mu_{Y_a})
\right|
\ge
4a\frac{(W/4)^r}{r!}.
}
\tag{23}
\]

Choose `a=a_r -> 1` and `W=L(1-o(1/r))`. Then `(W/L)^r -> 1`, so (23) and (14) meet and prove (1).

This lower argument is exact at the level of the full kernel. It does not require the `r`-th Taylor term to dominate all later terms; positivity of every derivative in (10) is carried through the divided difference instead.

## 4. Repetition gives a sharp PNT-small source capacity

A single level-set block already proves the normalized lower bound. To use essentially the full insertion budget, leave an arbitrarily small translation margin around `I` and repeat the block at distinct common translations. Translation preserves (18) by the binomial theorem, and every block has the same sign in (22).

At each fixed `p`, the translation parameters can be chosen generically so that all resulting real labels `q=Ue^{-z}` are distinct, avoid the ordinary primes, and avoid collisions between different blocks. If

\[
N_p
=\left\lfloor
\frac{\delta_pU}{r\log U}
\right\rfloor,
\qquad
m_p=N_pr,
\tag{24}
\]

and `delta_p U/(r log U) -> infinity`, then

\[
m_p
=(1+o(1))\delta_p\frac{U}{\log U}.
\tag{25}
\]

Equations (4), (5), (14), and (23) then give matching upper and lower asymptotics

\[
\operatorname{Cap}^{(r)}_p(L,\delta)
=
\left(\frac4{Z_p}+o(1)\right)
\delta_p
\frac{(L/4)^r}{r!\eta_p}.
\tag{26}
\]

Since `Z_p=2+o(1)` and `tau_r^r=r! eta_p`, equation (26) is exactly (2).

The controls remain coarse-PNT-small exactly as in `RE-157`--`RE-161`:

\[
|\pi_Q(x)-\pi(x)|\le m_p=o(U/\log U),
\]

and

\[
|\vartheta_Q(x)-\vartheta(x)|
\le(1+o(1))m_p\log U=o(U).
\]

For `r>=2`, (18) also matches the first placement moment exactly, so the two packets have identical total inserted logarithmic/Chebyshev mass after the terminal layer has been passed.

## 5. The transition criterion is now exact at exponential scale

Write

\[
F_p
:=
\left(
\frac{L}{4\tau_r(p)}
\right)^r.
\tag{27}
\]

The upper half of (26) immediately gives

\[
F_p=O(1),\quad\delta_p\to0
\quad\Longrightarrow\quad
\Delta\mathcal A_p=o(1).
\tag{28}
\]

Conversely, if `F_p -> infinity`, choose any vanishing budget with `delta_p F_p` bounded below by a positive constant and with `delta_p U/(r log U) -> infinity`; this is possible throughout the `RE-160` regime because `r=o(log U)` implies `r log U/U -> 0`. The level parameter `a` can then be adjusted inside `(0,1)` to tune the lower construction to any prescribed fixed separation. Hence

\[
\boxed{
F_p\to\infty
\quad\Longrightarrow\quad
\text{fixed Robin-source ambiguity survives with }\delta_p\to0.
}
\tag{29}
\]

The boundary is therefore governed by

\[
r\log\frac{L}{4\tau_r}.
\]

A ratio `L/(4 tau_r)` bounded at or below one is stable under every vanishing PNT budget; a ratio tending above one fast enough that the displayed logarithm diverges produces matched controls with order-one leverage. Using Stirling,

\[
4\tau_r
=4(r!\eta_p)^{1/r}
=\left(\frac4e+o(1)\right)r\eta_p^{1/r},
\]

which proves (3). The leading critical-order asymptotic from `RE-160` is unchanged, but its universal multiplicative uncertainty is removed.

## 6. Prior-art boundary and scope

The ingredients used to sharpen the capacity are classical outside this Robin normalization. Chebyshev interpolation/minimax geometry is classical, and the Markov--Krein/Tchebycheff-system literature studies extremal expectations under finitely many moment constraints. Prouhet--Tarry--Escott theory is likewise the classical equal-power-sum setting behind the earlier lower constructions. A targeted audit of moment-space extremality, Chebyshev--Markov--Stieltjes inequalities, Prouhet--Tarry--Escott constructions, and Robin/colossally-abundant work did not locate the terminal kernel `G_U`, the capacity law (26), or the sharp radius `4 tau_r`. The proof above reconstructs every load-bearing step directly, so no new external theorem is required and `SOURCES.md` needs no update.

This remains a matched generalized-source obstruction. It does not assert that the ordinary primes can be rearranged into Chebyshev level packets, does not construct a Robin counterexample, and does not replace the approximate-moment leakage obstruction of `RE-161`. Exact moment matching is essential to (6); once the lower moments are only approximate, their signed leakage can dominate the Chebyshev remainder exactly as `RE-161` warns.

The result does change the source-side frontier. For exact growing-order controls, there is no longer an unresolved universal-constant gap to optimize by better Prouhet packets or a sharper Taylor remainder: the terminal generalized-source capacity is asymptotically fixed by Chebyshev approximation. The remaining positive question is genuinely arithmetic again: whether the ordinary-prime/CA source supplies the factorial weighted precision or signed coupling needed to stay below this sharp capacity, rather than whether the generalized moment model itself was being estimated inefficiently.
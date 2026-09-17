# RE-182 — Every fixed Euler-jet depth remains non-rigid under bounded prime multiplicity

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + EXACT-FINITE-EULER-JET-MATCHING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-180-LOCAL-TARIFF-ATTAINED + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-178, RE-180, RE-181.

`RE-181` shows that exact matching of the Mertens boundary value and the first Euler boundary slope remains non-rigid even after the control is forced back onto ordinary primes with multiplicities in `{0,1,2}`. `RE-178` separately shows that any fixed number of scalar Euler jets is subcritical for the earlier KV-capacity argument, but it does not construct an honest prime control matching those jets exactly.

The finite-jet escape is in fact realizable at every fixed depth.

Fix an integer `K>=1`. For every sufficiently large selector scale `p` there exists an ordinary-prime-supported source `Q_{p,K}` with

\[
\boxed{m_{Q_{p,K}}(q)\in\{0,1,2\}}
\tag{1}
\]

such that, writing

\[
D_{Q_{p,K}}(s)
 :=
 \sum_q\bigl(m_{Q_{p,K}}(q)-1\bigr)[-\log(1-q^{-s})],
\tag{2}
\]

we have:

1. `Q_{p,K}` agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p subset [2p,3p]` and has no compensating modification below `16p`;
3. all right-boundary Euler jets through depth `K` match exactly,
   \[
   \boxed{
   D_{Q_{p,K}}^{(j)}(1+)=0,
   \qquad 0\le j\le K;
   }
   \tag{3}
   \]
4. the jet series are absolutely convergent at the boundary, so (3) is obtained by legitimate termwise differentiation rather than conditional rearrangement;
5. the Chebyshev discrepancy obeys, with a constant allowed to depend on `K`,
   \[
   \boxed{
   |\vartheta_{Q_{p,K}}(x)-\vartheta(x)|
   \ll_K \sqrt p\log p+(\log x)^3,
   \qquad x\ge2p,
   }
   \tag{4}
   \]
   and therefore for every fixed `b>0`,
   \[
   |\vartheta_{Q_{p,K}}(x)-\vartheta(x)|
   \ll_{b,K}x\exp[-bV(x)],
   \qquad
   V(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}};
   \tag{5}
   \]
6. before repair becomes visible, the `RE-173` normalized Robin coordinate still moves by order one,
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_{p,K})-\mathcal A_{p,8p}(P)\asymp1;
   }
   \tag{6}
   \]
7. the first repair generation is contained in a fixed `K`-dependent multiplicative window `[16p,C_Kp]`, uses
   \[
   \boxed{
   \Theta_K\!\left(\frac{\sqrt p}{\log p}\right)
   }
   \tag{7}
   \]
   modified primes in total, and contains both
   \[
   \Theta_K\!\left(\frac{\sqrt p}{\log p}\right)
   \]
   deletions and the same order of duplications.

Thus **no fixed finite list of Euler derivatives at `s=1` rigidifies the transient Robin prefix**, even when ordinary-prime support, nonnegative integer multiplicity, the hard multiplicity cap `{0,1,2}`, and every fixed KV relative envelope are imposed simultaneously. The selector-scale local deletion tariff isolated by `RE-180` remains attainable while arbitrarily many *fixed* boundary jets are matched exactly.

The proof is a finite-dimensional interpolation/quantization construction. The essential device is to recenter the raw Euler jets at each repair scale. After centering, their shell responses converge to a fixed Vandermonde matrix instead of becoming increasingly ill-conditioned powers of `log x`. This makes the two-shell quantizer of `RE-181` a `(K+1)`-shell quantizer with uniform conditioning for every fixed `K`.

## 1. Euler jets and a centered basis

For `j>=1` define the exact right-boundary kernels

\[
J_j(q)
 :=
 (-\log q)^j\sum_{n\ge1}n^{j-1}q^{-n},
\qquad
J_0(q):=H(q):=\log\frac q{q-1}.
\tag{8}
\]

Then

\[
\frac{d^j}{ds^j}[-\log(1-q^{-s})]_{s=1+}=J_j(q).
\tag{9}
\]

It is convenient to remove the alternating derivative sign:

\[
U_j(q):=(-1)^jJ_j(q).
\tag{10}
\]

For every fixed `K`, uniformly for `0<=j<=K`,

\[
\frac{U_j(q)}{H(q)}
 =
 (\log q)^j\left(1+O_K(q^{-1})\right).
\tag{11}
\]

Indeed both the numerator in (8) and `H(q)=sum_{n>=1}q^{-n}/n` have leading term `q^{-1}`, while the remaining geometric tails are `O_K(q^{-2})` for fixed `j`.

At a repair baseline `x=e^L` define the centered kernels

\[
C_{m,L}(q)
 :=
 \sum_{j=0}^{m}
 \binom mj(-L)^{m-j}U_j(q),
 \qquad 0\le m\le K.
\tag{12}
\]

Combining (11) with the binomial theorem gives, whenever `q` is a fixed multiplicative factor of `x`,

\[
\boxed{
\frac{C_{m,L}(q)}{H(q)}
 =
 (\log q-L)^m
 +O_K\!\left(\frac{L^m}{q}\right).
}
\tag{13}
\]

This change of coordinates is triangular and invertible, so exact vanishing of all centered residuals `m<=K` is equivalent to exact vanishing of the raw Euler jets `j<=K`.

The point of (13) is conditioning. Raw responses look like `1,L,L^2,...,L^K` and become badly scaled as the repair horizon moves. Centered responses at fixed multiplicative offsets remain `O_K(1)`.

## 2. A uniformly invertible `(K+1)`-shell response matrix

Choose fixed distinct shell factors

\[
c_r:=2^r,
\qquad 0\le r\le K,
\tag{14}
\]

and write `alpha_r=log c_r`. At baseline `x=e^L` consider the normalized response matrix

\[
A_x(m,r)
 :=
 \frac{C_{m,L}(c_rx)}{H(c_rx)},
 \qquad 0\le m,r\le K.
\tag{15}
\]

By (13),

\[
A_x(m,r)=\alpha_r^m+o_K(1)
\qquad(x\to\infty).
\tag{16}
\]

The limit matrix `[alpha_r^m]_{m,r=0}^K` is a Vandermonde matrix on distinct nodes, hence invertible. Consequently there are constants `x_*(K)` and `Lambda_K<infty` such that

\[
\boxed{
\|A_x^{-1}\|\le\Lambda_K
\qquad(x\ge x_*(K)).
}
\tag{17}
\]

Therefore any centered residual vector `rho=(rho_0,...,rho_K)` can be cancelled *over the reals* by signed shell `H`-masses `w_0,...,w_K` satisfying

\[
A_xw=\rho,
\qquad
\sum_{r=0}^K|w_r|\ll_K\|\rho\|_\infty.
\tag{18}
\]

This is the generic interpolation step. The arithmetic work is to realize the signed real masses by distinct ordinary primes with coefficients only `+1` or `-1`, while making the quantization error contract and keeping the Chebyshev discrepancy KV-small.

## 3. The first repair generation already attains the RE-180 deletion tariff

Let `D_p subset [2p,3p]` be the `RE-173` deletion packet and put

\[
d_p:=\sum_{q\in D_p}H(q)
\asymp\frac1{\sqrt p\log p}.
\tag{19}
\]

Take the first repair baseline

\[
x_0:=16p,
\qquad L_0:=\log x_0.
\tag{20}
\]

The deletion packet contributes `-1` at each `q in D_p`, so the repair target in the centered coordinates (12) is

\[
\rho_m^{(0)}
 :=
 \sum_{q\in D_p}C_{m,L_0}(q).
\tag{21}
\]

Because `q/x_0 in [1/8,3/16]`, equation (13) yields

\[
\|\rho^{(0)}\|_\infty\asymp_K d_p.
\tag{22}
\]

More importantly,

\[
\rho_0^{(0)}=d_p,
\qquad
\rho_1^{(0)}\le-c_0d_p
\tag{23}
\]

for an absolute `c_0>0` and all sufficiently large `p`. Every repair node in (14) has `alpha_r>=0`. Hence a real solution of (18) for the first generation cannot have only nonnegative weights: its first centered moment would then be nonnegative, contradicting (23).

If

\[
W_-:=-\sum_{w_r<0}w_r,
\qquad
W_+:=\sum_{w_r>0}w_r,
\tag{24}
\]

then the bounded range `0<=alpha_r<=K log 2`, together with (18), (23), gives

\[
\boxed{W_-\asymp_K d_p,\qquad W_+\asymp_K d_p.}
\tag{25}
\]

Thus the continuous interpolation problem itself already requires selector-scale positive and negative repair mass. The negative side is not an artefact of the two-jet construction.

Now replace each ideal node `c_rx_0` by a narrow prime shell

\[
I_{0,r}
 :=
 [c_rx_0,c_rx_0(1+\delta_{x_0})],
\qquad
\delta_x:=(\log x)^{-A_K},
\tag{26}
\]

with `A_K` a fixed sufficiently large constant. Ordinary PNT asymptotics give total available `H`-mass

\[
\sum_{q\in I_{0,r}}H(q)
\asymp_K\frac{\delta_{x_0}}{\log x_0},
\tag{27}
\]

which is much larger than `d_p`. Greedily choose distinct primes of coefficient `sgn(w_r)` until their `H`-mass approximates `|w_r|` to within one prime weight. Since `H(q)asymp_K1/p` on this first generation, the rounding error in each shell is `O_K(1/p)`.

Across a shell, (13) varies by

\[
O_K\!\left(\delta_x+\frac{(\log x)^K}{x}\right).
\tag{28}
\]

Therefore the first-generation centered residual after prime quantization is

\[
O_K\!\left(
\left[\delta_{x_0}+\frac{(\log x_0)^K}{x_0}\right]d_p
+\frac1{x_0}
\right),
\tag{29}
\]

strictly smaller than `d_p` for large `p`.

Because a selected negative prime is deleted once and a selected positive prime is duplicated once, all multiplicities remain in `{0,1,2}`. Equation (25) and `H(q)asymp_K1/p` imply that the first generation contains

\[
\Theta_K(pd_p)
=
\Theta_K\!\left(\frac{\sqrt p}{\log p}\right)
\tag{30}
\]

primes of each sign. This realizes, rather than merely evades, the selector-scale lower tariff of `RE-180`.

## 4. Geometric iteration drives every fixed jet residual exactly to zero

Choose a fixed scale ratio

\[
R_K>2^{K+2}
\tag{31}
\]

and baselines

\[
x_n:=R_K^nx_0,
\qquad L_n:=\log x_n.
\tag{32}
\]

The shell families `[c_rx_n,c_rx_n(1+delta_{x_n})]` are then pairwise disjoint across generations. At generation `n`, express the current residual in the centered basis at `L_n`, solve the uniformly conditioned real system (18), and quantize each signed shell mass by distinct ordinary primes as above.

Changing the centering point from `L_n` to `L_{n+1}=L_n+log R_K` is an exact finite binomial translation. For fixed `K` its operator norm is bounded by a constant depending only on `K` and `R_K`; it does not grow with `n`.

Let `M_n` denote the sup norm of the centered residual just before generation `n`. From (17), (28), the one-prime rounding error, and the bounded recentering map, we obtain

\[
M_{n+1}
\le
\varepsilon_nM_n+\frac{C_K}{x_n},
\tag{33}
\]

where `epsilon_n -> 0`. By increasing the starting threshold `p_0(K)` if necessary, we may arrange

\[
\varepsilon_n\le\theta_K<R_K^{-2}
\qquad(n\ge0).
\tag{34}
\]

Hence

\[
\boxed{
M_n
\ll_K
\theta_K^nd_p+rac1{x_{n-1}}
}
\tag{35}
\]

with the second term omitted at `n=0`. In particular `M_n -> 0`.

The total absolute `H`-mass inserted at generation `n` is `O_K(M_n+1/x_n)`. Since on that generation

\[
|J_j(q)|\ll_K(\log x_n)^jH(q),
\qquad 0\le j\le K,
\tag{36}
\]

we have

\[
\sum_{n\ge0}
(\log x_n)^K
\left(M_n+\frac1{x_n}\right)
<\infty.
\tag{37}
\]

Thus every jet series through order `K` converges absolutely. The residual tends to zero in the centered basis, hence also in the raw basis, and the infinite prime control satisfies the exact identities (3).

The infinite continuation is essential and is consistent with `RE-172`: already exact zeroth-coordinate Mertens matching forbids a nontrivial *finite* ordinary-prime perturbation. What is new here is that the infinite continuation can satisfy any prescribed fixed finite jet depth without giving up bounded prime multiplicity or KV fidelity.

## 5. Chebyshev accounting remains inside every fixed KV envelope

At generation `n`, a selected prime near `x_n` has `H(q)asymp_K1/x_n`. Therefore the total absolute Chebyshev mass of the generation is bounded by

\[
\ll_K
x_n\log x_n
\left(M_n+\frac1{x_n}\right).
\tag{38}
\]

Insert (35). The part propagated from the original selector debt contributes

\[
\ll_K
x_0d_p
\sum_{n\ge0}
(R_K\theta_K)^n\log x_n
\ll_K\sqrt p,
\tag{39}
\]

because `R_K theta_K<1` and `x_0d_p log p asymsqrt p`. The rounding-forcing part contributes only `O_K(log x_n)` per completed generation, so up to height `x` its cumulative absolute contribution is `O_K((log x)^2)`.

Together with the original `RE-173` selector packet, this gives the deliberately loose but convenient bound (4). Since

\[
\sqrt p\log p
=o\!\left(p e^{-bV(p)}\right)
\tag{40}
\]

for every fixed `b>0`, and every fixed power of `log x` is `o(xe^{-bV(x)})`, equation (5) follows after enlarging the implied constant over the finite initial range.

No repair appears below `16p`, so the order-one transient Robin displacement at horizon `8p` is exactly the one already established in `RE-173` and retained in `RE-181`. Matching more boundary jets does not retroactively change that prefix.

## 6. Representation audit and prior-art boundary

The linear-algebraic core is generic. After centering, matching `K+1` moments at `K+1` distinct nodes is precisely a Vandermonde/interpolatory-quadrature mechanism. That part should not be interpreted as new arithmetic structure. A prior-art search for finite moment matching, interpolatory quadrature, prescribed Euler-product derivatives, and generalized-prime boundary data found the expected classical Vandermonde/quadrature machinery, but no result identified in that search supplies the prime-shell construction above with coefficients restricted to `{-1,0,1}`, exact infinite residual removal, transient Robin ambiguity, and simultaneous KV fidelity. No external theorem beyond ingredients already used and sourced by the parent findings is load-bearing here, so `SOURCES.md` does not require a new anchor.

The arithmetic-specific ingredients are narrower and explicit:

- the exact Euler kernels (8) have the common asymptotic `H(q)(log q)^j` in (11);
- ordinary primes provide enough mass in the polylogarithmically thin *relative* shells (26), a regime already used in `RE-181` and far longer than a difficult short-prime interval;
- fresh prime shells permit coefficient signs `-1` and `+1` while keeping actual multiplicities in `{0,1,2}`;
- the geometric residual decay makes every boundary series absolutely convergent;
- the same decay converts the infinite exact-matching continuation into only bounded/polylogarithmic Chebyshev cost.

So the result is not that finite moment interpolation is special to Robin. The line-specific content is that the **ordinary-prime Euler boundary representation has enough shell freedom to realize that interpolation under the exact discrete source constraints that survived RE-180**.

## 7. Adversarial checks and exact boundary of the claim

Several stronger-looking statements do **not** follow.

First, `K` is fixed before `p -> infinity`. The constants `Lambda_K`, `R_K`, `A_K`, `C_K`, and the threshold `p_0(K)` may grow very rapidly with `K`. Nothing here is uniform for `K=K(p)`, and the proof gives no access to the crossover regime `K asymlog p/loglog p` identified in `RE-178`.

Second, this does not contradict the high-temperature rigidity of `RE-174`. A finite Taylor jet at one boundary point is strictly less information than an unbounded exact Euler-temperature profile. The construction leaves open the possibility that a growing jet family or a genuinely functional boundary observable rigidifies the source.

Third, the first-generation sign lower bound uses the geometry of the canonical selector packet relative to repair shells beginning at `16p`; it is not a universal theorem about arbitrary perturbations. Its role is to show that the specific local branch priced in `RE-180` is feasible at the same asymptotic cardinality while all fixed jets are matched.

Fourth, the result proves source non-rigidity, not RH or a Robin counterexample. The control source is deliberately matched to coarse boundary data while differing from the physical prime source in a transient prefix. Its purpose is to falsify a proposed information set as sufficient, not to claim that such a control is itself the arithmetic object of interest.

## Conclusion

`RE-181` is not a two-dimensional accident. For every fixed finite `K`, the boundary constraints

\[
D_Q^{(j)}(1+)=0,
\qquad 0\le j\le K,
\]

still leave enough ordinary-prime freedom to preserve an order-one transient Robin ambiguity under multiplicities `{0,1,2}` and every fixed KV envelope.

The remaining rigidity frontier therefore cannot be "add a few more Euler derivatives." A successful source-faithful obstruction must use information whose dimension grows with the selector scale, a genuinely functional/nonlocal Euler observable, a joint arithmetic constraint not reducible to finitely many scalar jets, or the actual CA/Robin selector geometry. `RE-178` located the first plausible growing-jet scale from capacity considerations; the present construction shows why **every fixed depth below that frontier is genuinely non-rigid, not merely unruled-out by the previous bound**.

# WI-111 — Bombieri--Vinogradov forces polynomial-dimensional full-packed near-nullity

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It strengthens the WI-105--WI-110 full-packing obstruction in a direction that WI-110 left open: the bad sector need not be one-dimensional. For every fixed exponent `0 < theta < 1/2`, there are simultaneous positive-defect fully packed prime interactions whose target-local processed concatenation has `asymp p^theta` bottom singular directions at a vanishing relative scale. Consequently, arbitrary global linear processing cannot obtain fixed conditioning and fixed normalized transmission merely by deleting `O(p^beta)` source directions for any fixed `beta < 1/2`.

More precisely, fix

\[
0<\theta<\frac12.
\tag{1}
\]

There are infinitely many odd source primes `p`, two distinct odd target primes

\[
p<q_1<q_2<\frac{4p}{3},
\tag{2}
\]

one common observation length `N`, and an odd integer `ell` such that

\[
\ell\asymp p^\theta,
\qquad
\Delta:=q_2-q_1=O(\ell\log p),
\tag{3}
\]

and both `(p,q_i,N)` lie in the genuinely positive-defect exact full-packing regime of WI-096/WI-102/WI-104. Put

\[
G_i=(U_p^{(N)})^*U_{q_i}^{(N)},
\qquad
K_i=\ker G_i^*\subset\mathbf C^{p-1}.
\tag{4}
\]

Then each `K_i` contains an explicit `(ell-1)`-dimensional subspace `W_i`, and after choosing orthonormal character bases the cross Gram of these two subspaces is exactly

\[
\boxed{
X_1^*X_2=\sqrt{\frac{t_2}{t_1}}\,I_{\ell-1},
\qquad
t_i=2p-q_i.
}
\tag{5}
\]

Thus all `ell-1` principal angles in this common character sector are equal and

\[
\boxed{
\sup_{\substack{x\in W_i\\ \|x\|=1}}
\operatorname{dist}(x,K_j)^2
\le
\frac{\Delta}{t_1}
\le
\frac{3\Delta}{2p}
=O\!\left(p^{\theta-1}\log p\right)
}
\tag{6}
\]

for `i ne j`.

Now permit the full target-local freedom of WI-108. For arbitrary finite-dimensional linear maps

\[
C_i:E_i\to\mathbf C^{q_i-1},
\qquad
B=[\,G_1C_1\;G_2C_2\,],
\tag{7}
\]

write the singular values of `B` in decreasing order, padding with zeros up to the source dimension `m=p-1`. If `B ne 0`, then

\[
\boxed{
\frac{\sigma_{p-\ell+1}(B)}{\sigma_1(B)}
\le
\sqrt{\frac{3\Delta}{2p}}
=O\!\left(p^{(\theta-1)/2}\sqrt{\log p}\right)
\longrightarrow0.
}
\tag{8}
\]

Hence at least `ell-1 asymp p^theta` source singular directions lie at vanishing relative scale, uniformly over **all** target-local right processing rules `C_1,C_2`.

The scale-sensitive WI-110 product law also extends index-by-index. For arbitrary finite-dimensional maps

\[
S:E\to\operatorname{dom}B,
\qquad
L:\mathbf C^{p-1}\to F,
\qquad
A=LBS,
\tag{9}
\]

and any index `k` for which `rank(A)>=k`, define

\[
r_k(A)=\frac{\sigma_k(A)}{\sigma_1(A)},
\qquad
\tau_B(L,S)=
\frac{\sigma_1(A)}{\|L\|_2\,\sigma_1(B)\,\|S\|_2}.
\tag{10}
\]

Then the singular-value ideal property gives

\[
\boxed{
r_k(A)\tau_B(L,S)
\le
\frac{\sigma_k(B)}{\sigma_1(B)}.
}
\tag{11}
\]

Therefore every processed system retaining

\[
k\ge p-\ell+1
\tag{12}
\]

source dimensions satisfies

\[
\boxed{
r_k(A)\tau_B(L,S)
\le
\sqrt{\frac{3\Delta}{2p}}
\longrightarrow0.
}
\tag{13}
\]

In particular, fix any `beta<1/2` and suppose a proposed linear rescue is allowed to delete at most

\[
d(p)=O(p^\beta)
\tag{14}
\]

source dimensions. Choose `theta` with `beta<theta<1/2`. Then `ell>d(p)+1` for all sufficiently large members of the counterfamily, so `k=p-1-d(p)>=p-ell+1`, and (13) applies. Such a rescue cannot simultaneously keep a fixed relative singular gap and transmit a fixed normalized fraction of the original operator scale.

## 1. Bombieri--Vinogradov supplies a growing quotient divisor

The new arithmetic ingredient is only the classical Bombieri--Vinogradov theorem. Let `X` tend to infinity and put

\[
Q=X^\theta.
\tag{15}
\]

Since `theta<1/2`, for every fixed logarithmic loss the Bombieri--Vinogradov level eventually contains all moduli up to `2Q`. In the standard maximal form, for every sufficiently large fixed `A`,

\[
\sum_{M\le2Q}
\max_{(a,M)=1}\max_{y\le2X}
\left|
\psi(y;M,a)-\frac{y}{\varphi(M)}
\right|
\ll_A \frac{X}{(\log X)^A}.
\tag{16}
\]

Restrict to moduli

\[
Q\le M\le2Q,
\qquad M\equiv2\pmod4.
\tag{17}
\]

There are `asymp Q` such moduli. If all but `o(Q)` are called good when the maximal error in (16) is at most a sufficiently small fixed multiple of `X/Q`, Markov's inequality applied to (16) shows that good moduli exist for every sufficiently large `X`. Choose one and write

\[
\boxed{M=2\ell.}
\tag{18}
\]

Then `ell` is odd and

\[
\ell\asymp Q\asymp X^\theta.
\tag{19}
\]

Take two disjoint fixed-proportion intervals, for example

\[
I_s=[X,1.05X],
\qquad
I_t=[1.10X,1.15X].
\tag{20}
\]

For the source residue `1 mod M` and the target residue

\[
a_t=\ell+2\pmod{2\ell},
\tag{21}
\]

both residue classes are reduced: `gcd(1,M)=1`, while `ell` odd gives

\[
\gcd(\ell+2,2\ell)=1.
\tag{22}
\]

For a good modulus, subtracting the two endpoint estimates in (16) gives von-Mangoldt mass `gg X/Q` in each interval and each of these residue classes. Prime powers contribute only `O(X^{1/2}\log X)` in total, whereas

\[
\frac{X}{Q}=X^{1-\theta}\gg X^{1/2}\log X.
\tag{23}
\]

Hence there is a source prime

\[
p\in I_s,
\qquad p\equiv1\pmod{2\ell},
\tag{24}
\]

and there are

\[
\gg\frac{X}{Q\log X}
\tag{25}
\]

target primes in `I_t` with

\[
q\equiv\ell+2\pmod{2\ell}.
\tag{26}
\]

Two consecutive such target primes may therefore be chosen with

\[
\boxed{
\Delta=q_2-q_1=O(Q\log X)=O(\ell\log p).
}
\tag{27}
\]

The interval separation in (20) gives `p<q_i`, and `q_i<=1.15X<4p/3` because `p>=X`. Also `p asymp X`, so (19) becomes `ell asymp p^theta`.

This is the only point at which a growing-modulus prime-distribution theorem is used. WI-105--WI-108 used a fixed modulus-three progression; replacing it by a Bombieri--Vinogradov-selected modulus lets the quotient-character multiplicity grow polynomially while retaining two nearby targets.

## 2. The congruences force `ell` independent quotient characters into both kernels

Put

\[
d_i=q_i-p,
\qquad
h_i=\frac{d_i}{2},
\qquad
t_i=2p-q_i=p-d_i.
\tag{28}
\]

Equations (24) and (26) give

\[
d_i\equiv\ell+1\pmod{2\ell},
\tag{29}
\]

so

\[
h_i\equiv\frac{\ell+1}{2}\pmod\ell,
\qquad
\ell\mid t_i.
\tag{30}
\]

Choose an integer center `c` satisfying

\[
h_2<c<p-h_2,
\qquad
c\equiv\frac{\ell+1}{2}\pmod\ell.
\tag{31}
\]

The interval in (31) has length `t_2>2p/3`, while `ell=o(p)`, so such a `c` exists. Define

\[
\rho_i=c-h_i.
\tag{32}
\]

Then

\[
0<\rho_i<t_i,
\qquad
\boxed{\ell\mid\rho_i,\quad\ell\mid t_i.}
\tag{33}
\]

Consequently

\[
g_i:=\gcd(\rho_i,t_i)\ge\ell.
\tag{34}
\]

For each target choose `k_i mod p` with

\[
k_id_i\equiv\rho_i\pmod p
\tag{35}
\]

and set

\[
r_i=k_iq_i+d_i+\rho_i.
\tag{36}
\]

Exactly as in WI-105/WI-107,

\[
r_i\equiv2\rho_i+d_i=2c\pmod p.
\tag{37}
\]

Because `gcd(pq_1,pq_2)=p`, the generalized Chinese remainder theorem supplies one `N` with

\[
N\equiv r_i\pmod{pq_i}
\qquad(i=1,2).
\tag{38}
\]

The complementary nearest-boundary case is handled by the exact source-phase translation of WI-104, so both actual full-packed holes have starts `rho_i` and the common center `c`. Since `g_i>=ell>1`, both interactions have positive defect.

WI-104 identifies the actual source kernel as the augmentation hyperplane on the cyclic quotient of order `g_i`. Its unwrapped exterior interval is

\[
I_i=[\rho_i-t_i,\rho_i-1],
\qquad |I_i|=t_i.
\tag{39}
\]

Since `ell|g_i`, every nontrivial character of `Z/ell Z` pulls back to an allowed quotient character. For `1<=a<ell`, define

\[
f_{i,a}=0\quad\text{on the hole},
\qquad
f_{i,a}(w\bmod p)=e(aw/\ell)
\quad(w\in I_i).
\tag{40}
\]

Then `f_{i,a} in K_i`. Because `ell|t_i`, the vectors

\[
x_{i,a}=t_i^{-1/2}f_{i,a},
\qquad 1\le a<\ell,
\tag{41}
\]

are orthonormal. Let

\[
W_i=\operatorname{span}\{x_{i,a}:1\le a<\ell\}.
\tag{42}
\]

Thus

\[
\boxed{\dim W_i=\ell-1.}
\tag{43}
\]

## 3. The two large defect sectors are exactly isoclinic

Because the full-packed holes are concentric and `q_1<q_2`, WI-104 gives

\[
I_2\subset I_1,
\qquad |I_i|=t_i,
\qquad t_1-t_2=q_2-q_1=\Delta.
\tag{44}
\]

For `1<=a,b<ell`, equations (40)--(41) yield

\[
\langle x_{1,a},x_{2,b}\rangle
=\frac1{\sqrt{t_1t_2}}
\sum_{w\in I_2}e((b-a)w/\ell).
\tag{45}
\]

The interval length `t_2` is divisible by `ell`. Hence the geometric sum vanishes for `a ne b`, while for `a=b` it equals `t_2`. Therefore

\[
\boxed{
\langle x_{1,a},x_{2,b}\rangle
=\sqrt{\frac{t_2}{t_1}}\,\delta_{ab},
}
\tag{46}
\]

which is (5).

In particular, for every `x in W_1`, its orthogonal projection onto `W_2 subset K_2` has norm

\[
\|P_{W_2}x\|^2=\frac{t_2}{t_1}\|x\|^2.
\tag{47}
\]

Thus

\[
\operatorname{dist}(x,K_2)^2
\le
\left(1-\frac{t_2}{t_1}\right)\|x\|^2
=\frac{\Delta}{t_1}\|x\|^2.
\tag{48}
\]

The same bound holds with the two indices reversed. Since `q_1<4p/3`,

\[
t_1>\frac{2p}{3},
\tag{49}
\]

and (6) follows from (27).

This is stronger than WI-105's single shared order-three character. The pair `(W_1,W_2)` has `ell-1` equal small principal angles, with `ell` itself growing like `p^theta`.

## 4. Courant--Fischer turns the character sector into many small singular values

Write

\[
\widetilde G_i=G_iC_i,
\qquad
b_i=\|\widetilde G_i\|_2,
\tag{50}
\]

and choose `i_*` so that `b_{i_*}=max(b_1,b_2)`. Target-local right processing preserves every original left-kernel vector:

\[
K_i\subseteq\ker\widetilde G_i^*.
\tag{51}
\]

For any unit vector `x in W_{i_*}`, the own block vanishes. If `j ne i_*`, project `x` onto `K_j` and use (6):

\[
\|\widetilde G_j^*x\|
\le
b_j\operatorname{dist}(x,K_j)
\le
b_{i_*}\sqrt{\frac{3\Delta}{2p}}.
\tag{52}
\]

Hence on the entire `(ell-1)`-dimensional subspace `W_{i_*}`,

\[
\|B^*x\|
\le
b_{i_*}\sqrt{\frac{3\Delta}{2p}}\,\|x\|.
\tag{53}
\]

The Courant--Fischer min--max principle for the eigenvalues of `BB^*` therefore gives

\[
\sigma_{p-\ell+1}(B)
\le
b_{i_*}\sqrt{\frac{3\Delta}{2p}}.
\tag{54}
\]

On the other hand

\[
\sigma_1(B)\ge b_{i_*}.
\tag{55}
\]

If `b_{i_*}=0`, then `B=0` and the conclusion is trivial; otherwise (54)--(55) prove (8). No information about the nonzero singular values inside the individual blocks is used.

The index is exact: the source dimension is `m=p-1`, while `dim W_{i_*}=ell-1`, so the min--max index is

\[
m-(\ell-1)+1=p-\ell+1.
\tag{56}
\]

## 5. Fixed-power source deletion is not a free escape from WI-110

The singular-value ideal inequality used by WI-110 holds at every index:

\[
\sigma_k(LBS)
\le
\|L\|_2\,\sigma_k(B)\,\|S\|_2.
\tag{57}
\]

Multiplying the two normalized factors in (10) gives (11) exactly. If a global selector drops `d` source dimensions but still produces rank

\[
k=p-1-d,
\tag{58}
\]

then (12) is equivalent to

\[
d\le\ell-2.
\tag{59}
\]

Under this condition, (8), (11), and monotonicity of the singular values give (13).

Now let `d(p)=O(p^beta)` with `beta<1/2`. Since `theta` in (1) is arbitrary below `1/2`, choose

\[
\beta<\theta<\frac12.
\tag{60}
\]

The Bombieri--Vinogradov construction has `ell asymp p^theta`, so (59) holds eventually. If a proposed processed system has

\[
r_k(A)\ge c>0,
\tag{61}
\]

then necessarily

\[
\tau_B(L,S)
\ll_c p^{(\theta-1)/2}\sqrt{\log p}
\longrightarrow0.
\tag{62}
\]

Conversely, fixed normalized transmission forces `r_k(A)->0`. Therefore neither rectangular selection, pseudoinverse-type mixing, nor any other linear pre/post-processing can evade the full-packed obstruction by sacrificing only `O(p^beta)` source dimensions with `beta<1/2` while retaining scale.

This strictly extends WI-110, which kept all `p-1` source dimensions. It also sharpens the interpretation of restricted-invertibility as a possible escape: **some** dimension loss can always alter conditioning, but the present arithmetic counterfamily forces the number of simultaneously weak directions to grow as any prescribed fixed power below `p^(1/2)`.

## 6. Boundaries and falsification controls

The exponent `1/2` comes from the classical Bombieri--Vinogradov level used to select a growing congruence modulus. The theorem does **not** assert that `p^(1/2)` is a true barrier for the Ramanujan geometry. Stronger distribution of primes in arithmetic progressions could enlarge the quotient divisor and therefore the number of near-null directions. Conversely, no result beyond Bombieri--Vinogradov is being smuggled into (1)--(62).

The construction remains a uniform finite-window counterfamily. The generalized CRT observation length can be very large, and no positive analytic density of such exact full-packed windows is claimed. Thus the finding rules out uniform coercivity theorems derived solely from this algebraic interface; it does not prove that these windows dominate the actual Yang covariance or zeta-zero statistics.

The result also does not close **macroscopic** source deletion. A selector discarding a fixed positive proportion of the `p-1` source dimensions lies outside (14), as does a deletion scale at or beyond the distributional range used here. Such a route would have to explain why losing that much source information is still compatible with the desired arithmetic main term.

Positive slack away from exact full packing, extra source normalization, nonlinear processing, or arithmetic information that changes the operator before the finite-window compression also remain outside the claim. Nothing here identifies the uncertified complement of zeta zeros as multiple, off-line, or pure proof slack.

## 7. Prior art and novelty boundary

The prime-distribution input is classical. E. Bombieri, **On the large sieve**, *Mathematika* 12 (1965), 201--225, DOI `10.1112/S0025579300005313`, is an original source for the large-sieve mean distribution theorem now called Bombieri--Vinogradov; standard modern treatments include H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge University Press, 2006. The only use here is the existence of a modulus `M asymp X^theta`, `theta<1/2`, on which two specified reduced residue classes have the expected prime mass in fixed-proportion intervals.

The min--max step is the classical Courant--Fischer principle for singular values, and the ideal inequality (57) is the same standard singular-value `s`-number property already used in WI-110. Björck--Golub principal-angle theory is already anchored in WI-105. The equal-angle structure (46) is an instance of the classical isoclinic-subspace notion; see P. W. H. Lemmens and J. J. Seidel, **Equi-isoclinic subspaces of Euclidean spaces**, *Indagationes Mathematicae (Proceedings)* 76:2 (1973), 98--107, DOI `10.1016/1385-7258(73)90042-5`. Ramanujan-subspace terminology and exact-period character spaces remain classical as recorded in `SOURCES.md` through Vaidyanathan.

A targeted search around Bombieri--Vinogradov-selected Ramanujan subspaces, growing principal-angle multiplicity, isoclinic finite-window Ramanujan kernels, restricted invertibility, and source-dimension deletion did not locate this arithmetic specialization. That negative search is **not** a priority claim. The durable contribution is the exact combination of WI-104's quotient-character kernel normal form with a growing Bombieri--Vinogradov congruence modulus and Courant--Fischer: the WI-105 near-parallel phenomenon can occupy polynomially many source directions, not merely one character pair.

## 8. Program consequence

WI-110 left rank-reducing rectangular selection as a genuine linear escape because its sharp transmission law tracked only the smallest source singular value while requiring retention of all source dimensions. The present finding removes the bounded- and sub-square-root-power codimension version of that escape.

For every fixed `beta<1/2`, a theorem claiming that **all** fully packed prime Ramanujan interactions can be made uniformly coercive with nonvanishing normalized scale after discarding only `O(p^beta)` source directions is false. The counterfamily may be chosen with `theta` strictly between `beta` and `1/2`, producing more weak directions than the selector is allowed to delete.

A genuinely new linear escape must therefore pay one of three prices that are absent from the current full-packed interface: discard a much larger source sector, exploit positive slack/additional arithmetic information that destroys the quotient-character alignment, or use an analytic normalization strong enough to compensate the vanishing scale of the surviving weak singular sector. Merely replacing WI-110's all-source pseudoinverse by a low-codimension restricted inverse is no longer a scale-free way around the obstruction.
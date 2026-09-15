# NB-138 — polynomially tight simple clusters inherit the target-poor confluent barrier

**Status:** `DERIVED + QUANTITATIVE-CONFLUENT-TRANSFER + GROWING-SIMPLE-CLUSTER + TARGET-AWARE-GRASSMANN-CONTROL + EXPLICIT-POLYNOMIAL-SPACING + MATCHED-ZERO-ENVELOPE-CONTROL + REPRESENTATION-AUDIT + NEGATIVE/METHOD-BOUNDARY`.

`NB-137` proves that a growing cluster of distinct simple states can be made arbitrarily close, as a subspace, to the target-poor confluent packet of `NB-111` while its ordinary natural-prefix power matrix becomes arbitrarily ill-conditioned. Its spacing choice is deliberately existential: for every height `G` one first asks for some unknown continuity radius `epsilon_*(G,eta_G)` and then chooses the split spacing below it. That leaves open whether the target-poor transfer only occurs at fantastically small, nonquantified separations.

The continuity radius can in fact be made explicit enough for the source comparison. The one-state map used by `NB-137` is uniformly holomorphic in a fixed complex tube around the real vertical-displacement axis. Combining its Cauchy derivative bounds with the Laguerre-normalized coercivity from `NB-111` gives a quantitative perturbation theorem for the whole growing packet.

Fix

\[
r\ge 1,\qquad q\ge 2,\qquad 0<a<\frac12,
\tag{1}
\]

and a constant

\[
0<c<\frac18.
\tag{2}
\]

Put

\[
m_G=\lceil G\rceil,\qquad R_G=m_Gq,\qquad
d_G=\lfloor c\log G\rfloor,
\tag{3}
\]

and retain the analytic one-state family `w_G(h)` and target `e_G` of `NB-137`. For a positive spacing `epsilon_G`, define

\[
\mathcal S_G^{\rm split}
=\operatorname{span}\{w_G(j\varepsilon_G):0\le j<d_G\},
\tag{4}
\]

and let

\[
\mathcal S_G^{\rm conf}
=\operatorname{span}\{w_G^{(j)}(0):0\le j<d_G\}.
\tag{5}
\]

Set

\[
D_a:=1+\frac{4(1-a)}a=\frac4a-3.
\tag{6}
\]

Then the explicit sufficient condition

\[
\boxed{
\varepsilon_G\,
G^{c\log D_a}
(\log G)^{25/2}
\longrightarrow0
}
\tag{7}
\]

implies

\[
\boxed{
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\longrightarrow0.
}
\tag{8}
\]

In particular, for every fixed

\[
\boxed{
B>c\log D_a,
}
\tag{9}
\]

the polynomial spacing

\[
\boxed{
\varepsilon_G=G^{-B}
}
\tag{10}
\]

already forces the distinct simple packet to inherit the target-poor confluent limit.

If in addition `c<0.10076`, the same formal packet lies below the right-half local zero-count allowance used in `NB-133`--`NB-137`. For `(10)` its ordinary natural-prefix zero-power matrix nevertheless satisfies

\[
\boxed{
\log\kappa_2(V_G)
\ge
(cB+o(1))(\log G)^2.
}
\tag{11}
\]

Thus the matched control of `NB-137` does **not** require a superexponentially or nonconstructively tiny split. A fixed polynomial phase cell already supports the coexistence of catastrophic ordinary-coordinate conditioning and vanishing target access.

## 1. The one-state family is uniformly holomorphic in a fixed tube

The cell space is

\[
\mathcal E_{r,R_G}
=\operatorname{span}\{\phi_n:r\le n<R_G\},
\qquad
\phi_n(t)=e^{-t/2}\mathbf 1_{[\log n,\log(n+1))}(t),
\tag{12}
\]

with

\[
\|\phi_n\|_2^2
=\frac1n-\frac1{n+1}
=\frac1{n(n+1)}.
\tag{13}
\]

Extend the real displacement in `NB-137` to a complex variable `z=x+iy` by

\[
\langle\phi_n,w_G(z)\rangle
=
\sqrt{2a}\,m_G^{a+iG+iz}
\int_n^{n+1}
 t^{-a-iG-iz-3/2}\,dt.
\tag{14}
\]

Only real `z` will represent split packet states; the complex extension is a proof device for derivative control.

Write

\[
b=a-y,\qquad \tau=G+x.
\tag{15}
\]

On the fixed tube `|y|<=a/2`,

\[
\frac a2\le b\le\frac{3a}{2}<\frac34.
\tag{16}
\]

For bounded real `x` and large `G`, `|tau|\asymp G`. Evaluating the elementary antiderivative in `(14)` therefore gives

\[
\left|
\int_n^{n+1}t^{-b-i\tau-3/2}\,dt
\right|
\ll_a
\frac{n^{-b-1/2}}G.
\tag{17}
\]

Consequently

\[
|\langle\phi_n,w_G(z)\rangle|
\ll_a
\frac{m_G^b}{G}\,n^{-b-1/2}.
\tag{18}
\]

Using the orthogonality of the cells and `(13)`,

\[
\begin{aligned}
\|w_G(z)\|_2^2
&=
\sum_{n=r}^{R_G-1}
\frac{|\langle\phi_n,w_G(z)\rangle|^2}
     {\|\phi_n\|_2^2}\\
&\ll_{a,r}
\frac{m_G^{2b}}{G^2}
\sum_{n< R_G}n^{1-2b}\\
&\ll_{a,q,r}
\frac{m_G^{2b}R_G^{2-2b}}{G^2}
\ll_{a,q,r}1.
\end{aligned}
\tag{19}
\]

The constants are uniform for `b` in the compact interval `(16)`. Hence the finite-dimensional Hilbert-valued map `z -> w_G(z)` is uniformly bounded on disks of radius `a/2` centred at every sufficiently small real displacement. Cauchy's estimate gives

\[
\boxed{
\|w_G^{(k)}(h)\|_2
\le
C_{a,q,r}\,k!\left(\frac2a\right)^k
}
\tag{20}
\]

whenever `|h|<=1` and `G` is large enough. The important point is that `(20)` has no hidden power of `G`.

## 2. Divided differences approximate the whole jet at a controlled rate

For `0<=j<d_G`, define the forward divided-difference columns exactly as in `NB-137`,

\[
v_{j,G}(\varepsilon)
=
\varepsilon^{-j}
\sum_{\ell=0}^{j}
(-1)^{j-\ell}\binom j\ell
w_G(\ell\varepsilon).
\tag{21}
\]

Repeated use of the fundamental theorem of calculus gives the Banach-valued identity

\[
\boxed{
v_{j,G}(\varepsilon)
=
\int_{[0,1]^j}
 w_G^{(j)}\!\left(
 \varepsilon(t_1+\cdots+t_j)
 \right)
 dt_1\cdots dt_j.
}
\tag{22}
\]

For `d_G\varepsilon<=1`, `(20)` therefore yields

\[
\boxed{
\|v_{j,G}(\varepsilon)-w_G^{(j)}(0)\|_2
\le
C_{a,q,r}\,
\varepsilon\,j(j+1)!
\left(\frac2a\right)^{j+1}.
}
\tag{23}
\]

Raw derivative columns are the wrong coordinates in which to compare `(23)` with the target coercivity of `NB-111`, because their scales themselves vary rapidly with the derivative order. The useful normalization is already present canonically in that finding: use the orthonormal Laguerre polynomial basis.

Let `L_k` denote the standard Laguerre polynomials and set

\[
p_k(u)
:=
L_k\!\left(-\frac{1-a}{a}u\right).
\tag{24}
\]

Under the change of variables in `NB-111`, this is exactly the polynomial state whose Laguerre coordinate is `Q=L_k`. If `g_{k,G}` denotes its confluent state, the expansion

\[
L_k(x)
=
\sum_{j=0}^{k}
(-1)^j\binom kj\frac{x^j}{j!}
\tag{25}
\]

and the identity from `NB-137`,

\[
w_G^{(j)}(0)
=
\left(-\frac{i}{2a}\right)^j w_{j,G},
\tag{26}
\]

give

\[
\boxed{
g_{k,G}
=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 w_G^{(j)}(0).
}
\tag{27}
\]

Define the corresponding split columns by replacing the derivative in `(27)` with the divided difference,

\[
\widetilde g_{k,G}(\varepsilon)
:=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 v_{j,G}(\varepsilon).
\tag{28}
\]

The map from the `v_j` to the `\widetilde g_k` is triangular with nonzero diagonal. The map from the raw simple states to the `v_j` is also triangular and invertible whenever `epsilon != 0`. Therefore

\[
\boxed{
\operatorname{span}\{\widetilde g_{k,G}(\varepsilon):k<d_G\}
=
\mathcal S_G^{\rm split}(\varepsilon).
}
\tag{29}
\]

No information is discarded by the normalization.

Combining `(23)` and `(28)`, and writing

\[
D_a=1+\frac{4(1-a)}a,
\]

gives

\[
\begin{aligned}
\|\widetilde g_{k,G}-g_{k,G}\|_2
&\ll_{a,q,r}
\varepsilon
\sum_{j=1}^{k}
\binom kj
\left(\frac{4(1-a)}a\right)^j
j(j+1)\\
&\ll_{a,q,r}
\boxed{\varepsilon\,k^2D_a^k}.
\end{aligned}
\tag{30}
\]

This is the quantitative replacement for the unspecified continuity radius `epsilon_*(G,eta_G)` in `NB-137`.

## 3. Laguerre coercivity turns column control into a target-angle bound

Let

\[
A_G:\mathbb C^{d_G}\to\mathcal E_{r,R_G},
\qquad
A_G\alpha
=
\sum_{k<d_G}\alpha_k g_{k,G},
\tag{31}
\]

and similarly let `B_G(epsilon)` synthesize the split columns `(28)`.

Because the `L_k` are orthonormal in `L^2(e^{-z}dz)`, the coefficient vector in `(31)` has exactly the Laguerre norm used in `NB-111`. Since `c<1/8`, the logarithmic-rank hypothesis of that finding holds with a fixed margin. Its coercive estimate therefore gives, with

\[
\eta_G=(\log m_G)^{-10},
\tag{32}
\]

\[
\boxed{
\|A_G\alpha\|_2
\ge
c_{a,q,r,c}\,\eta_G\|\alpha\|_2
}
\tag{33}
\]

for all large `G`. In particular,

\[
\sigma_{\min}(A_G)\gg_{a,q,r,c}(\log G)^{-10}.
\tag{34}
\]

From `(30)`, a crude Frobenius bound is already enough:

\[
\boxed{
\|B_G(\varepsilon)-A_G\|
\ll_{a,q,r}
\varepsilon\,d_G^{5/2}D_a^{d_G}.
}
\tag{35}
\]

Define

\[
\theta_G
:=
C_{a,q,r,c}
\varepsilon_G\,d_G^{5/2}D_a^{d_G}
(\log G)^{10}.
\tag{36}
\]

If `theta_G->0`, then `(33)`--`(35)` imply that `B_G` retains full rank and every unit vector `y` in its range lies within

\[
\frac{\theta_G}{1-\theta_G}
\tag{37}
\]

of the confluent range. Indeed, writing `y=B_G\alpha/\|B_G\alpha\|`, the distance to `Ran(A_G)` is at most `||(B_G-A_G)alpha||/||B_G alpha||`, while

\[
\|B_G\alpha\|
\ge
\bigl(\sigma_{\min}(A_G)-\|B_G-A_G\|\bigr)\|\alpha\|.
\tag{38}
\]

The target projection can be written as a supremum over unit vectors in the state range. Hence

\[
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\le
\frac{\|P_{\mathcal S_G^{\rm conf}}e_G\|}
     {\|e_G\|}
+
\frac{\theta_G}{1-\theta_G}.
\tag{39}
\]

The first term tends to zero by `NB-111`. Since

\[
d_G=c\log G+O(1),
\qquad
D_a^{d_G}
=G^{c\log D_a+o(1)},
\tag{40}
\]

condition `(7)` makes `theta_G->0` and proves `(8)`.

For the polynomial choice `(10)`, `(36)` becomes

\[
\theta_G
\ll
G^{-(B-c\log D_a)+o(1)}
(\log G)^{25/2},
\tag{41}
\]

so every `B` satisfying `(9)` is sufficient. The constant is not optimized. What matters is the qualitative upgrade from an unspecified diagonal spacing in `NB-137` to an explicit **fixed power of the height**.

## 4. The same polynomial cluster is still superpolynomially ill-conditioned in ordinary power coordinates

Let the formal simple points be

\[
\rho_{j,G}
=
\frac12+a+i(G+j\varepsilon_G),
\qquad 0\le j<d_G,
\tag{42}
\]

and form the complete natural-prefix power matrix

\[
V_G
=
\left(n^{-\overline{\rho_{j,G}}}\right)_
{1\le n\le R_G,\ 0\le j<d_G}.
\tag{43}
\]

`NB-137` derives, with `M_G=d_G-1`, the exact binomial finite-difference bound

\[
\kappa_2(V_G)
\ge
C_a^{-1}
\binom{2M_G}{M_G}^{1/2}
(\varepsilon_G\log R_G)^{-M_G}.
\tag{44}
\]

Substituting `epsilon_G=G^{-B}`, `R_G\asymp G`, and `M_G=c\log G+O(1)` gives

\[
\begin{aligned}
\log\kappa_2(V_G)
&\ge
M_G\bigl(B\log G-\log\log R_G\bigr)
+O(M_G)\\
&=
\boxed{(cB+o(1))(\log G)^2},
\end{aligned}
\tag{45}
\]

which is `(11)`. Thus a packet can be explicitly close enough to its confluent target-poor state space while ordinary coefficient recovery is worse than every fixed power of `G`.

This separates three scales that were conflated before `NB-137`: the raw simple-root coefficient scale, the confluent/Hermite state-space scale, and the target angle. Equation `(45)` is about the first; `(29)` preserves the second; `(39)` controls the third.

## 5. Matched source control: current zero laws still permit the polynomial cell

The result above is deterministic state geometry. To compare it with the source information used in the recent zero-packet findings, now also assume

\[
0<c<0.10076.
\tag{46}
\]

Then the packet `(42)` contains

\[
d_G=(c+o(1))\log G
\tag{47}
\]

right-half points and has vertical diameter

\[
(d_G-1)\varepsilon_G
=O(G^{-B}\log G)
=o(1).
\tag{48}
\]

Reapplying the same explicit Riemann--von Mangoldt endpoint-error envelope used in `NB-112`, `NB-132`, `NB-133`, and `NB-137` to a window of width `(48)` still allows

\[
(0.20152+o(1))\log G
\tag{49}
\]

zeros in the full critical strip. After functional-equation pairing, the corresponding right-half allowance is

\[
(0.10076+o(1))\log G,
\tag{50}
\]

so `(47)` lies strictly below it. The fixed horizontal position `1/2+a<1` also remains safely to the left of the Vinogradov--Korobov zero-free boundary for large `G`.

Therefore the coarse source inputs used by `NB-133`--`NB-137` do not exclude a packet with the explicit polynomial separation `(10)`. This remains a **matched control**, not a claim that actual zeta zeros realize `(42)`. To eliminate this control, genuinely new arrangement information is needed: for example a deterministic spacing or local-cluster theorem strong enough to prevent `Theta(log G)` right-half zeros from entering a polynomial phase cell of the size required by `(9)`.

A targeted literature search found the expected classical theory of divided differences, Hermite/confluent Vandermonde interpolation, and modern clustered-Vandermonde/superresolution conditioning. Those sources explain the general numerical phenomenon but do not provide the Nyman target estimate `(39)`. A separate search for unconditional deterministic lower bounds on distances between distinct zeta zeros did not locate a theorem that rules out the polynomial matched cells above. No external result is load-bearing here: the analytic-tube bound `(19)`, the divided-difference estimate `(23)`, and the perturbation estimate `(39)` are derived directly, while the only source envelopes are already canonical dependencies of the preceding findings. `SOURCES.md` therefore requires no new anchor.

## 6. Representation audit, falsification tests, and remaining boundary

The complex extension in `(14)` introduces no new state into the claim. It is used only to obtain the Cauchy estimate `(20)`; the split packet itself consists exclusively of the real-displacement states in `(4)`. Likewise, `(27)` and `(28)` are invertible changes of coordinates within the confluent and split packet ranges. The decisive conclusion `(8)` is the orthogonal target projection onto the original split range and is therefore invariant under those coordinate choices.

The fastest internal falsification tests are quantitative. First, `(19)` can be checked directly from the exact cell norm `(13)` and the antiderivative in `(17)`; any hidden growth in `G` would invalidate the polynomial threshold. Second, the factorial in the Cauchy derivative estimate must cancel against the `1/j!` in the Laguerre expansion `(27)`. If it did not, the perturbation cost would grow like `exp(Theta(log G log log G))` and `(10)` would no longer follow. Third, `NB-111` must be applied in the Laguerre-normalized coordinates, not to the raw derivative columns; `(24)`--`(33)` make that normalization explicit.

The exponent threshold `c log D_a` is only sufficient and is not claimed to be sharp. It comes from a deliberately crude Cauchy radius `a/2`, the columnwise estimate `(30)`, and a Frobenius bound. Better analytic radii or a direct operator estimate could enlarge the admissible phase cell. None of that changes the present structural conclusion: **target-poor confluence is already stable under an explicit polynomial splitting at logarithmic packet rank**.

This sharpens the next source-specific question. `NB-136` showed that full natural-prefix oversampling does not stabilize ordinary inversion; `NB-137` showed qualitatively that the resulting singularity can be target-irrelevant; `NB-138` now removes the nonquantified-spacing escape. What remains is not another sampling argument but an arrangement theorem for actual zeros, or a target-aware certificate that works outside the polynomial confluence cell and is insensitive to the simple-versus-confluent parameterization.
# NB-093 — single-zero growing-depth Gram gain is rank-one causal-state leverage

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + ELEMENTARY-BLASCHKE + RANK-ONE-GRAM-UPDATE + EXACT-NORMALIZED-CORRELATION-BRIDGE + GROWING-DEPTH + NEGATIVE-METHOD-BOUNDARY`.

`NB-092` finds a genuinely source-sensitive effect at growing multiplicative depth. For the canonical Möbius annulus direction, one off-critical zero `rho=beta+i gamma`, `beta>1/2`, already forces a generalized visible-Gram gain of size `q^(2 beta-1)`. The unresolved point there is diagonal normalization: the radial observable is built from a correlation Gram, so rowwise energy inflation may absorb the unnormalized determinant gain.

For a **single** Blaschke factor this open bridge has an exact finite-dimensional form. An elementary half-plane Blaschke factor is a one-state causal all-pass filter. At any finite physical cutoff, removing that factor changes the entire visible Gram matrix by **one positive rank-one outer product**. Consequently the polynomial determinant gain of `NB-092` is carried by exactly one generalized eigenvalue, and diagonal normalization reduces to an explicit comparison between one inverse-correlation leverage and the coordinatewise energies of the same causal state.

Let

\[
\rho=\beta+i\gamma,
\qquad
\lambda=\rho-\frac12,
\qquad
a=\Re\lambda=\beta-\frac12>0,
\tag{1}
\]

and use the elementary factor

\[
b_\lambda(z)=\frac{z-\lambda}{z+\overline\lambda}
=1-\frac{2a}{z+\overline\lambda},
\qquad z=s-\frac12.
\tag{2}
\]

For the raw Nyman innovations from `NB-088`,

\[
\widetilde D_j(s)
=
\frac{\zeta(s)}s
\bigl(j^{1-s}-(j+1)^{1-s}\bigr),
\tag{3}
\]

define the one-zero partially deflated innovations

\[
D_j^{(\rho)}:=\frac{\widetilde D_j}{b_\lambda}.
\tag{4}
\]

This is a legitimate Hardy vector because `rho` is an actual zero of `zeta`; equivalently, if the full Burnol factor is `B=b_lambda B'`, then `D_j^(rho)=B'D_j`.

Fix any finite index set `I` and any physical cutoff `R>1`. Write

\[
A_R
:=
\bigl(\langle J_R\widetilde D_i,J_R\widetilde D_j\rangle\bigr)_{i,j\in I},
\qquad
K_R^{(\rho)}
:=
\bigl(\langle J_RD_i^{(\rho)},J_RD_j^{(\rho)}\rangle\bigr)_{i,j\in I}.
\tag{5}
\]

Then there is an explicit state vector `s_R=(s_(j,R))_(j in I)` such that

\[
\boxed{
K_R^{(\rho)}=A_R+s_Rs_R^*.
}
\tag{6}
\]

Thus

\[
\boxed{
\operatorname{rank}\bigl(K_R^{(\rho)}-A_R\bigr)\le1,
\qquad
K_R^{(\rho)}\succeq A_R.
}
\tag{7}
\]

If `A_R>0`, the complete generalized spectrum of the pair is

\[
\operatorname{Spec}
\left(A_R^{-1/2}K_R^{(\rho)}A_R^{-1/2}\right)
=
\{1+\tau_R,1,\ldots,1\},
\tag{8}
\]

where

\[
\boxed{
\tau_R=s_R^*A_R^{-1}s_R.
}
\tag{9}
\]

In particular,

\[
\boxed{
\frac{\det K_R^{(\rho)}}{\det A_R}=1+\tau_R.
}
\tag{10}
\]

For the growing-depth band and Möbius annulus vector of `NB-092`, this one scalar already carries the full polynomial single-zero gain. More precisely, for `R=mq` and the coefficient vector

\[
c_j=\frac1m S_{\lfloor j/m\rfloor},
\qquad
S_r=\sum_{d\le r}\frac{\mu(d)}d,
\qquad m\le j<mq,
\tag{11}
\]

one has the exact state coupling

\[
\boxed{
|s_R^*c|^2
=
\frac{2a}{m|\rho|^2}
\left|q^\lambda-q^{-1/2}\right|^2.
}
\tag{12}
\]

Since `NB-092` gives

\[
c^*A_Rc=\frac1m\left(1-\frac1q\right),
\tag{13}
\]

it follows that

\[
\boxed{
\tau_R
\ge
\frac{2a}{|\rho|^2}
\frac{|q^\lambda-q^{-1/2}|^2}{1-1/q}
=
q^{2a+o(1)}.
}
\tag{14}
\]

Hence the `q^(2 beta-1)` determinant repair found in `NB-092` is not a many-mode volume phenomenon for one zero: it is exactly a **one-state leverage blow-up**.

The normalized-correlation bridge is equally explicit. Put

\[
a_j:=(A_R)_{jj},
\qquad
u_j:=\frac{|s_{j,R}|^2}{a_j},
\qquad
D:=\operatorname{diag}(a_j),
\qquad
z:=D^{-1/2}s_R,
\tag{15}
\]

and let

\[
\widetilde{\mathcal R}_R=D^{-1/2}A_RD^{-1/2}
\tag{16}
\]

be the raw correlation Gram. Then

\[
\tau_R=z^*\widetilde{\mathcal R}_R^{-1}z,
\tag{17}
\]

while exact diagonal normalization gives

\[
\boxed{
-\log\det\mathcal R_R^{(\rho)}
+
\log\det\widetilde{\mathcal R}_R
=
\sum_{j\in I}\log(1+\nu_j)
-
\log(1+\tau_R).
}
\tag{18}
\]

Equation `(18)` is the missing exact interface left open by `NB-092` for one zero. A proof that the unnormalized gain survives normalization must compare the **same** causal state in two geometries: coordinate energy `sum log(1+nu_j)` versus inverse-correlation leverage `log(1+tau_R)`. The determinant lower bound alone cannot decide that comparison.

## 1. One elementary Blaschke factor has one finite-prefix leakage state

The forward causal realization of `(2)` in Paley--Wiener time is

\[
(M_{b_\lambda}x)(t)
=
x(t)
-2a\int_0^t e^{-\overline\lambda(t-v)}x(v)\,dv.
\tag{19}
\]

Let `T=log R`, let `P=J_R` be restriction to `[0,T]`, and put `Q=I-P`. For a partially deflated innovation

\[
x_j:=D_j^{(\rho)},
\qquad
y_j:=M_{b_\lambda}x_j=\widetilde D_j,
\tag{20}
\]

causality gives

\[
PM_{b_\lambda}Px_j=Py_j.
\tag{21}
\]

For `t>T`, the input `Px_j` has stopped, so `(19)` becomes

\[
QM_{b_\lambda}Px_j(t)
=
-2a e^{-\overline\lambda(t-T)}r_{j,R},
\tag{22}
\]

where

\[
r_{j,R}
:=
\int_0^T e^{-\overline\lambda(T-v)}x_j(v)\,dv.
\tag{23}
\]

Define the unit tail mode

\[
h_R(t)
:=
\sqrt{2a}\,e^{-\overline\lambda(t-T)}\mathbf1_{(T,\infty)}(t)
\tag{24}
\]

and the scalar state

\[
s_{j,R}:=\sqrt{2a}\,r_{j,R}.
\tag{25}
\]

Because `||h_R||_2=1`, equation `(22)` is simply

\[
QM_{b_\lambda}Px_j=-s_{j,R}h_R.
\tag{26}
\]

Multiplication by `b_lambda` is an isometry. Therefore, for every pair `i,j`,

\[
\begin{aligned}
\langle Px_i,Px_j\rangle
&=
\langle M_{b_\lambda}Px_i,M_{b_\lambda}Px_j\rangle\\
&=
\langle Py_i,Py_j\rangle
+s_{i,R}\overline{s_{j,R}}.
\end{aligned}
\tag{27}
\]

This proves the rank-one identity `(6)` without an asymptotic, a zero-density estimate, or any assumption on the other zeros of `zeta`.

The state can also be written using only the **raw** prefix. From `(19)`, the state in `(23)` obeys

\[
r'(t)=\lambda r(t)+y_j(t),
\qquad r(0)=0,
\tag{28}
\]

so

\[
\boxed{
s_{j,R}
=
\sqrt{2a}
\int_0^{\log R}
 e^{\lambda(\log R-v)}\widetilde d_j(v)\,dv.
}
\tag{29}
\]

Moreover `\widetilde D_j(\rho)=0`. Hence the complete Laplace integral at `lambda` vanishes and `(29)` is equivalently the scaled missing tail

\[
\boxed{
s_{j,R}
=
-\sqrt{2a}\,R^\lambda
\int_{\log R}^{\infty}
 e^{-\lambda v}\widetilde d_j(v)\,dv.
}
\tag{30}
\]

Thus the state vector is not an arbitrary rank-one perturbation inserted after the fact. It is the finite-horizon remainder of the actual zeta zero condition, sampled simultaneously across the Nyman innovations.

## 2. Matrix determinant gain is exactly one generalized eigenvalue

Assume the raw finite Gram `A_R` is positive definite, as it is for the consecutive visible bands used in `NB-091`--`NB-092`. Applying the matrix determinant lemma to `(6)` gives

\[
\det(A_R+s_Rs_R^*)
=
\det A_R\left(1+s_R^*A_R^{-1}s_R\right),
\tag{31}
\]

which is `(10)`. The generalized matrix is

\[
A_R^{-1/2}K_R^{(\rho)}A_R^{-1/2}
=
I+vv^*,
\qquad
v=A_R^{-1/2}s_R,
\tag{32}
\]

and therefore has one eigenvalue `1+||v||^2=1+tau_R` and all remaining eigenvalues exactly one.

This sharpens the interpretation of `NB-092`. There, positivity was enough to infer a determinant lower bound from one amplified Rayleigh quotient. For a single zero there is no hidden distribution of that gain over the rest of the spectrum: **there is no rest of the source-specific generalized spectrum**. Everything contributed by that elementary factor at the cutoff is encoded by `tau_R`.

For the annulus vector `(11)`, translate the raw flat profile from `NB-092` by `log m`. On `0<=u<log q`,

\[
f_m(u)=m^{-1/2}e^{-u/2}.
\tag{33}
\]

Using `(29)` at the final horizon `u=log q`, linearity of the state gives

\[
\begin{aligned}
r_c
&=
\frac1{\sqrt m}
\int_0^{\log q}
 e^{\lambda(\log q-u)}e^{-u/2}\,du\\
&=
\frac1{\sqrt m}
\frac{q^\lambda-q^{-1/2}}{\lambda+1/2}\\
&=
\frac1{\sqrt m}
\frac{q^\lambda-q^{-1/2}}{\rho}.
\end{aligned}
\tag{34}
\]

Since `s_c=s_R^*c` up to the harmless inner-product convention, `(12)` follows. Dividing by `(13)` and using the variational definition of `tau_R` proves `(14)`.

The leading exponent is exactly

\[
2a=2\beta-1.
\tag{35}
\]

Thus the zero-frontier exponent identified in `NB-092` is now attached to an explicit causal-state leverage rather than only to an unnormalized determinant inequality.

## 3. Diagonal normalization is an exact leverage-versus-coordinate-energy test

The rank-one identity also removes the ambiguity in equation `(49)` of `NB-092`. From `(6)`,

\[
(K_R^{(\rho)})_{jj}
=a_j+|s_{j,R}|^2
=a_j(1+\nu_j).
\tag{36}
\]

Combining `(10)` and `(36)` with

\[
\det\mathcal R
=
\frac{\det K}{\prod_j K_{jj}}
\tag{37}
\]

gives

\[
\frac{\det\mathcal R_R^{(\rho)}}
     {\det\widetilde{\mathcal R}_R}
=
\boxed{
\frac{1+\tau_R}
     {\prod_j(1+\nu_j)}
}.
\tag{38}
\]

Taking minus logarithms gives `(18)`.

The two terms have different meanings. The quantity

\[
\sum_j\log(1+\nu_j)
\tag{39}
\]

is what independent diagonal rescaling would charge for the state energy seen one coordinate at a time. By contrast,

\[
\tau_R
=
z^*\widetilde{\mathcal R}_R^{-1}z
\tag{40}
\]

measures the same state against the **inverse raw correlation geometry**. It can be large because `z` aligns with a raw near-kernel even when no individual coordinate energy is large.

Accordingly, the next theorem cannot be merely another lower bound for `det K/det A`: `(10)` already makes that quantity exact. To obtain a positive centered entropy excess one would need

\[
\prod_j(1+\nu_j)
\gg
1+\tau_R,
\tag{41}
\]

with quantitative divergence; to prove a negative centered excess one would need the reverse inequality. Either conclusion is now a concrete Nyman-specific statement about the state vector `(29)` and the raw correlation inverse.

There is no abstract implication from large `tau_R` to either sign. As a matched linear-algebra control, take `A_R` diagonal and let `s_R` be supported on one coordinate. Then `tau_R=nu_k` for that coordinate and

\[
\frac{\det\mathcal R_R^{(\rho)}}
     {\det\widetilde{\mathcal R}_R}
=1
\tag{42}
\]

exactly, even if `tau_R` is arbitrarily large. Thus an arbitrarily large unnormalized determinant gain can be removed completely by diagonal normalization. This does not model the actual Nyman correlation geometry; it proves that the `NB-092` determinant gain alone is logically insufficient to cross the normalized bridge.

## 4. A finite Blaschke divisor is a finite-rank causal-state update

The one-state identity iterates. Let

\[
B_F=\prod_{r=1}^d b_{\lambda_r}
\tag{43}
\]

be any fixed finite Blaschke divisor, with multiplicity, and successively divide the raw innovations by its `d` elementary factors. At each step the visible Gram changes by one positive rank-one state outer product. Therefore there are vectors `s^(1),...,s^(d)` such that

\[
\boxed{
K_R^{[F]}
=A_R+
\sum_{r=1}^d s^{(r)}s^{(r)*}
=A_R+SS^*,
}
\tag{44}
\]

where `S` has at most `d` columns. In particular,

\[
\boxed{
K_R^{[F]}-A_R\succeq0,
\qquad
\operatorname{rank}(K_R^{[F]}-A_R)\le d.
}
\tag{45}
\]

The determinant ratio is consequently the `d x d` state determinant

\[
\boxed{
\frac{\det K_R^{[F]}}{\det A_R}
=
\det\left(I_d+S^*A_R^{-1}S\right).
}
\tag{46}
\]

If `Z=D^{-1/2}S` and `z_j^*` denotes the `j`th row of `Z`, then the normalized bridge generalizes to

\[
\boxed{
-\log\det\mathcal R_R^{[F]}
+
\log\det\widetilde{\mathcal R}_R
=
\sum_j\log\left(1+\|z_j\|^2\right)
-
\log\det\left(I_d+Z^*\widetilde{\mathcal R}_R^{-1}Z\right).
}
\tag{47}
\]

This finite-state structure reconciles the two regimes already established by the line. `NB-088`--`NB-090` show that finitely many off-critical defects can be asymptotically silent on fixed terminal horizons. `NB-092` shows that one zero becomes polynomially visible when the relative horizon grows. Equations `(44)`--`(47)` show that growing depth changes the **size** of the finite state, not its dimension: a fixed set of `d` zeros can repair at most `d` generalized Gram directions at any cutoff.

The genuinely infinite Burnol product is therefore qualitatively different only if its effective state dimension or aggregate leverage grows with the horizon. A proof based on a fixed finite divisor cannot manufacture a high-rank entropy source by going deeper; it can only make its finitely many state directions larger.

## 5. Prior-art, novelty, and falsification boundary

The abstract ingredients are classical. An elementary Blaschke factor is a degree-one scalar inner/all-pass function with a one-dimensional state/model-space defect; finite Blaschke products have finite-dimensional model spaces. The matrix determinant lemma and finite-rank determinant reduction are standard linear algebra. A targeted audit of classical all-pass state-space factorization and Hardy model-space literature confirms that this finite-state mechanism should not be claimed as a new operator-theoretic theorem.

The closest Nyman-specific literature already tracked by the line remains Burnol's Blaschke/Hardy decomposition and Ziad's finite Blaschke versus arithmetic Gram split in `SOURCES.md`; recent smoothed/multiscale Gram work likewise studies a different geometry. The audit did not locate the exact finite-prefix identity `(6)`, the explicit annulus state coupling `(12)`, or the normalized leverage identity `(18)` specialized to the canonical consecutive Nyman innovations. No priority claim is made. Because the proof here is the explicit one-state realization `(19)` plus finite-dimensional algebra, no new external theorem is load-bearing and `SOURCES.md` is unchanged.

The main adversarial boundaries are strict. First, `(6)` concerns one **actual zero factor** or a finite divisor of the actual Burnol product; it does not replace the full infinite product by a finite approximation. Second, a rank-one unnormalized update does not imply a rank-one change of the diagonally normalized correlation matrix, because the diagonal rescaling acts on every coordinate. Third, `(18)` does not assert the sign of the centered correlation excess. Fourth, the polynomial lower bound `(14)` is a lower bound on inverse-correlation leverage, not yet on the radial charge of `NB-086`. Fifth, the finite-degree extension `(44)` allows the state vectors at successive factors to depend on the intermediate partially deflated source; only the rank and positivity statement is universal.

The durable delta after `NB-092` is therefore exact: **a single off-critical zero contributes one causal state and one generalized Gram eigenvalue, and the entire diagonal-normalization problem is the scalar competition `(18)` between that state's rowwise energy and its leverage against the raw Nyman correlation inverse**. The next useful theorem should estimate that competition for the canonical state `(29)` or show that the full infinite Blaschke product creates a genuinely growing state-rank effect. Repeating an unnormalized determinant argument cannot settle the normalized radial frontier.
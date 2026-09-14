# MC-299 — A near-negative Page exception expands the balanced source-cost band by a `log log log` factor

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the Legendre-shell and source-cost notation of `MC-293`. Write

\[
L_1=\log y,
\qquad
L_2=\log\log y,
\qquad
L_3=\log\log\log y.
\tag{1}
\]

Assume the unique possible low-source-cost exceptional shell functional `\lambda_*` from `MC-293` actually exists and is near-negative at the live scale

\[
d_{\lambda_*}\le \frac{a}{L_2}
\tag{2}
\]

for some fixed `a>0`. Let `\chi_*` be the primitive real Dirichlet character carrying its Landau--Siegel zero

\[
\beta_*=1-\delta_*.
\tag{3}
\]

Then `MC-293` gives

\[
\delta_*\ll_a \frac{1}{L_1L_2}.
\tag{4}
\]

For every fixed `A>0` there is a sufficiently small constant `\kappa_A=\kappa_A(a)>0` such that, with

\[
E_y
:=
\exp\!\left(
\kappa_A\frac{L_1L_3}{L_2}
\right),
\tag{5}
\]

all sufficiently large `y` satisfy

\[
\boxed{
\sup_{\substack{\lambda\ne0,\lambda_*\\
                 \mathcal Q(\lambda)\le E_y}}
|x_\lambda|
\ll_{A,a}
(\log y)^{-A}.
}
\tag{6}
\]

Thus the existence of the single bad Page mode is self-isolating: its exceptionally close real zero forces, through the Deuring--Heilbronn phenomenon, much stronger balance for every *other* shell mode throughout a source-cost range strictly larger than the original Landau--Page range

\[
D_y
=
\exp\!\left(
\kappa_0\frac{L_1}{L_2}
\right)
\tag{7}
\]

of `MC-293`. Indeed, for fixed positive `\kappa_A,\kappa_0`,

\[
\frac{\log E_y}{\log D_y}
\asymp
L_3
\longrightarrow\infty.
\tag{8}
\]

Consequently, if `\tau<1/2` stays separated from `1/2` by more than `(\log y)^{-A}`, then

\[
\boxed{
\#\{\lambda\ne0:
      \mathcal Q(\lambda)\le E_y,
      \ d_\lambda\le\tau\}
\le1,
}
\tag{9}
\]

and the only possible member is `\lambda_*`. In particular, for any linearly independent near-negative family at defect scale `O(1/L_2)`, all but at most one direction must satisfy

\[
\boxed{
\mathcal Q(\lambda)>E_y.
}
\tag{10}
\]

This strictly strengthens the source-cost conclusion of `MC-293` *conditional on the exceptional shell mode actually being near-negative*. It does not eliminate `\lambda_*`, does not control source costs beyond `E_y`, and does not imply a bound for `M(x)`.

## 1. The exceptional mode supplies an unusually close zero

By `MC-293`, a near-negative exceptional shell functional is represented on the shell by a unique primitive real character `\chi_*` of conductor

\[
q_*\le 4D_y
\tag{11}
\]

whose real zero obeys `(4)`. The precise origin of `(4)` matters: it comes from the observed shell bias of `\lambda_*`, not from a conjectural bound on an arbitrary exceptional zero.

The gain below uses this quantitative closeness as input. A generic Landau--Page exception with no stronger estimate on `1-\beta_*` would not give the same enlarged source band.

## 2. Put the exceptional and target characters in one modulus

Let `\lambda\ne0,\lambda_*` have source cost

\[
m:=\mathcal Q(\lambda)\le E_y.
\tag{12}
\]

Choose a minimum-cost lower-prime representative as in `MC-293`, and write

\[
\chi(n)=\prod_{p\in V}\left(\frac np\right),
\qquad
\operatorname{cond}(\chi)=m.
\tag{13}
\]

The shell projector uses the two primitive characters

\[
\psi_0=\chi,
\qquad
\psi_1=\chi_4\chi,
\tag{14}
\]

of conductors `m` and `4m`, respectively. For each `j\in\{0,1\}`, put

\[
q_j
:=
\operatorname{lcm}
\bigl(q_*,\operatorname{cond}(\psi_j)\bigr).
\tag{15}
\]

Then

\[
q_j\le q_*\operatorname{cond}(\psi_j)
\le 16D_yE_y,
\tag{16}
\]

so

\[
\log q_j
\le
O\!\left(\frac{L_1}{L_2}\right)
+
\kappa_A\frac{L_1L_3}{L_2}.
\tag{17}
\]

Both `\chi_*` and `\psi_j` induce characters modulo `q_j`. If a primitive character `\varphi` of conductor `f\mid q_j` is induced to modulus `q_j`, then

\[
L(s,\widetilde\varphi)
=
L(s,\varphi)
\prod_{p\mid q_j,\ p\nmid f}
\bigl(1-\varphi(p)p^{-s}\bigr).
\tag{18}
\]

For `\Re s>0`, the finite Euler factors in `(18)` cannot cancel a zero of the primitive `L`-function near `1`. Hence `\beta_*` is also a zero of

\[
\mathscr L_{q_j}(s)
:=
\prod_{\rho\ ({\rm mod}\ q_j)}L(s,\rho).
\tag{19}
\]

Moreover, `(4)` and `(17)` give

\[
\delta_*\log q_j
\ll_a
\frac{L_3}{L_2^2}
\longrightarrow0.
\tag{20}
\]

Therefore, for all sufficiently large `y`,

\[
\beta_*
>
1-\frac{1}{10\log q_j},
\tag{21}
\]

so the explicit Deuring--Heilbronn theorem applies at the common modulus `q_j`.

The target characters in `(14)` are not the exceptional primitive character. If one of them equalled `\chi_*`, then on every shell prime `r\equiv1\pmod4` it would induce the same sign pattern as `\lambda_*`; since the occupied shell cells generate `H`, this would force `\lambda=\lambda_*`, contrary to assumption.

## 3. Deuring--Heilbronn creates a logarithmic-width zero-free strip

Benli, Goel, Twiss and Zaman, *Explicit Deuring--Heilbronn phenomenon for Dirichlet L-functions* (Proc. Amer. Math. Soc. 154 (2026), 509--525; DOI `10.1090/proc/17450`; arXiv `2410.06082v3`), Corollary 1.1, proves the following explicit form. If `q>400000`, `T\ge4`, and `\beta_1` is a real zero of `\mathscr L_q` with

\[
\beta_1>1-\frac{1}{10\log q},
\]

then every other zero `\rho=\beta+i\gamma` of `\mathscr L_q` with `\beta>1/2` and `|\gamma|\le T` satisfies

\[
1-\beta
>
\frac{
\log\!\left(
\dfrac{1}{16(1-\beta_1)
(10\log q+\log T+107)}
\right)
}
{10\log q+\log T+107}.
\tag{22}
\]

Take

\[
T=L_1^B
\tag{23}
\]

with `B` a fixed large constant to be chosen from `A`. Set

\[
H_j
:=
10\log q_j+\log T+107.
\tag{24}
\]

From `(4)`, `(17)`, and `(23)`,

\[
\delta_*H_j
\ll_{a,B}
\kappa_A\frac{L_3}{L_2^2}+o(1).
\tag{25}
\]

Thus

\[
\log\frac{1}{16\delta_*H_j}
\ge L_3
\tag{26}
\]

for sufficiently large `y`. At the same time, after `y` passes a threshold depending on `\kappa_A`, the `E_y` term dominates the fixed `D_y` term in `(17)`, and

\[
H_j
\ll
\kappa_A\frac{L_1L_3}{L_2}.
\tag{27}
\]

Combining `(22)`, `(26)`, and `(27)` gives a zero-free strip for every nonexceptional target character:

\[
\boxed{
\Re\rho
\le
1-c_A\frac{L_2}{L_1}
\qquad
(|\Im\rho|\le L_1^B),
}
\tag{28}
\]

where `c_A` can be made as large as any prescribed fixed constant by taking `\kappa_A` sufficiently small. More explicitly, the argument yields `c_A\gg1/\kappa_A` once `y` is sufficiently large.

This is the source of the `L_3` enlargement. The repulsion numerator in `(22)` is of order `L_3`, while allowing

\[
\log q\asymp\frac{L_1L_3}{L_2}
\]

puts the same `L_3` in the denominator; the two cancel and leave the classical power-logarithmic width `L_2/L_1` needed for strong prime-sum cancellation.

## 4. The zero-free strip gives uniform shell balance

Use the standard truncated explicit formula for a primitive nonprincipal Dirichlet character `\psi` of conductor `Q`:

\[
\psi(x,\psi)
:=
\sum_{n\le x}\Lambda(n)\psi(n)
=
-\sum_{\substack{L(\rho,\psi)=0\\|\Im\rho|\le T}}
\frac{x^\rho}{\rho}
+
O\!\left(
\frac{x\log^2(QxT)}{T}
+
\log(Qx)
\right),
\tag{29}
\]

with the standard harmless treatment of trivial zeros and endpoints. This is classical explicit-formula machinery; see, for example, Montgomery--Vaughan, *Multiplicative Number Theory I*, Chapters 12--14.

For either target character `\psi_j`, every nontrivial zero with `|\Im\rho|\le T` is also a zero of `\mathscr L_{q_j}`. Zeros with real part at most `1/2` are negligible here; all other zeros satisfy `(28)`. Standard zero counting then gives, uniformly for `x\asymp y`,

\[
\psi(x,\psi_j)
\ll
x\exp(-c_A L_2)\,L_1^{O(1)}
+
\frac{xL_1^2}{L_1^B}.
\tag{30}
\]

Choose first `B` sufficiently large in terms of `A`, and then choose `\kappa_A` sufficiently small so that `c_A` absorbs the fixed logarithmic losses in `(30)`. This yields

\[
\psi(x,\psi_j)
\ll_{A,a}
\frac{x}{L_1^{A+4}}
\qquad
(y\le x\le2y).
\tag{31}
\]

Prime powers contribute only `O(\sqrt y\,L_1^2)`, hence

\[
\sum_{y<p\le2y}\psi_j(p)\log p
\ll_{A,a}
\frac{y}{L_1^{A+4}}.
\tag{32}
\]

The exact shell projector from `MC-293` is

\[
T_\lambda(y)
=
\frac12
\sum_{y<p\le2y}
\bigl(\psi_0(p)+\psi_1(p)\bigr)\log p,
\tag{33}
\]

so `(32)` gives the same bound for `T_\lambda(y)`. Partial summation over `[y,2y]` yields

\[
A_\lambda
\ll_{A,a}
\frac{y}{L_1^{A+5}}.
\tag{34}
\]

Since

\[
N
\sim
\frac{y}{2L_1},
\tag{35}
\]

we obtain a bound stronger than `(6)` and hence `(6)` itself.

No GRH is used. The only zero information beyond the unconditional standard theory is the *consequence* of the near-negative exceptional mode already derived in `MC-293`, fed into the unconditional Deuring--Heilbronn theorem.

## 5. Consequence for the current Page-spectrum frontier

`MC-293` showed that at source cost at most `D_y`, all but at most one shell mode are balanced. `MC-294`--`MC-295` then showed that finite Fourier/coding information by itself permits the remaining near-negative family to escape into genuinely high-source-cost quotient directions. `MC-297`--`MC-298` showed that generic finite-order defect-overlap information does not close that escape either.

The present result adds a new arithmetic feedback mechanism. If the sole Page exception is actually strong enough to participate in a near-negative family, it cannot coexist passively with the other modes: the corresponding zero is so close to `1` that Deuring--Heilbronn repulsion enlarges the balanced source-cost band from

\[
\exp\!\left(O\!\left(\frac{L_1}{L_2}\right)\right)
\]

to

\[
\exp\!\left(O\!\left(\frac{L_1L_3}{L_2}\right)\right).
\tag{36}
\]

Thus any surviving multi-mode obstruction must pay a stronger arithmetic cost than `MC-293` recorded. The high-cost quotient escape remains possible, but its threshold moves outward by an unbounded `L_3` factor in the logarithm of the source conductor.

This does **not** solve the collective capacity problem: the finite models of `MC-295` can still assign arbitrarily expensive source directions, and `MC-298` remains a valid obstruction to bounded-order overlap reconstruction. What changes is the arithmetic admission threshold for those expensive directions in the exceptional branch.

## 6. Prior art and novelty audit

The zero-repulsion mechanism is classical Deuring--Heilbronn theory. The quantitative theorem `(22)` is exactly Corollary 1.1 of Benli--Goel--Twiss--Zaman; no novelty is claimed for it. The use of Deuring--Heilbronn to improve prime-number-theorem estimates in the presence of an exceptional zero is also standard and is central, for example, to Linnik-type arguments. Thorner and Zaman, *Refinements to the prime number theorem for arithmetic progressions* (Math. Z. 306 (2024), article 54; arXiv `2108.10878`), explicitly combine zero repulsion, zero-density estimates, and prime-distribution estimates in a much broader setting.

The Mathia-specific derived content is the parameter bridge:

1. shell near-negativity of `\lambda_*` forces the exceptional gap `\delta_*\ll1/(L_1L_2)` by `MC-293`;
2. source representatives of another shell mode and the exceptional character fit into a common modulus of size at most their conductor product;
3. substituting those two scales into explicit Deuring--Heilbronn repulsion leaves a zero-free width `\gg L_2/L_1` all the way to source conductors `\exp(cL_1L_3/L_2)`;
4. the standard explicit formula converts that width back into shell balance.

The literature search found the general ingredients and stronger general prime-distribution frameworks, but no reason to treat this specialization or the `log log log` threshold as an independent novel theorem. It is therefore classified as `LITERATURE+DERIVED` and `NO-NOVELTY-CLAIM`.

## 7. Boundaries and adversarial checks

### The result is conditional on the *existence* of a near-negative exception

If no `\lambda_*` exists, or if its defect is not `O(1/L_2)`, `(4)` is unavailable and this finding does not extend `MC-293`. The statement is an exceptional-branch feedback theorem, not a uniform replacement for Landau--Page.

### The exceptional mode itself survives

Deuring--Heilbronn repels *other* zeros. It does not move `\beta_*` or balance `\lambda_*`. The cardinality bound `(9)` therefore remains `1`, not `0`.

### Common-modulus inflation is included

The repulsion theorem is stated for characters modulo one common `q`. Equation `(16)` explicitly pays the product-conductor cost required to place the exceptional and target primitive characters in the same modulus. The `L_3` gain survives that inflation; it is not obtained by incorrectly applying a fixed-modulus theorem across unrelated conductors.

### Both parity representatives are controlled

The shell sum uses `\chi` and `\chi_4\chi`. The argument applies Deuring--Heilbronn separately to the two common moduli in `(15)`; controlling only one representative would not prove `(6)`.

### Polylogarithmic truncation height is load-bearing

The explicit formula needs only `T=(\log y)^B` to obtain an arbitrary fixed power of logarithmic saving. Taking `T\asymp y` would enlarge the denominator in `(22)` and obscure the gain. No high-zero information is silently discarded: the standard truncated explicit formula pays the tail explicitly through the `x/T` term.

### The new band is still subpolynomial

Because

\[
\frac{L_3}{L_2}\to0,
\]

one has

\[
E_y=y^{o(1)}.
\tag{37}
\]

The result does not control polynomial-conductor source characters, let alone the full high-source-cost quotient allowed by the finite models.

### No zeta zero is assumed away

The proof neither assumes RH nor shifts `1/\zeta(s)` into a desired zero-free half-plane. It uses an unconditional theorem about the consequences of a hypothetical Dirichlet exceptional zero and standard explicit-formula estimates for Dirichlet characters.

## Consequence

The current arithmetic escape is narrower than after `MC-298`. Bounded-order overlap data still cannot reconstruct Page parity, but a near-negative low-cost Page exception itself forces every *other* near-negative direction beyond

\[
\exp\!\left(
\kappa_A
\frac{\log y\,\log\log\log y}{\log\log y}
\right).
\]

The next viable collective route must therefore either control the capacity/realizability of source directions beyond this enlarged band, exploit information whose order grows with Page cardinality, or find a Möbius-specific identity that bypasses the generic parity barrier. The present result supplies arithmetic rigidity on the first axis but does not close it.
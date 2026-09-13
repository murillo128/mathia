# FD-094 — normalized Schur-energy records upgrade frontier carriers to fixed occupation

**Status:** `EXACT-DERIVED + RECORD-NORMALIZATION + FIXED-OCCUPATION-UPGRADE + ODD-CHANNEL + DYADIC-NONHEAD + COMPOSITION-REDUCTION + FALSE-RH-FRONTIER`.

`FD-090`--`FD-093` leave a specific composition defect. After exact repeated-prime transport one can produce a lower nonsquarefree mask whose energy has the full frontier exponent, but the complete lower state may be larger by a subpower factor. Thus the mask-to-state ratio is not known to stay bounded below by a fixed constant, and the fixed-occupation packet theorem cannot simply be restarted from that lower horizon.

That defect disappears at normalized Schur-energy records. The reason is elementary but structurally useful: the carrier estimates of `FD-090`, `FD-091`, and `FD-093` are already normalized by the same power of the destination horizon as the complete Schur energy. If the parent horizon is a record for that normalized complete energy, no lower destination can possess a larger normalized denominator. The frontier-normalized carrier inequality therefore upgrades automatically to a **fixed projective occupation inequality**.

More generally, the only loss is the parent's backward record defect. This identifies a sharper residual than the generic phrase "full exponent need not imply fixed occupation": for all repairable channels, the composition loss is quantitatively bounded by how far the parent lies below its historical normalized-energy maximum. At a true record the loss is absent. The row-two/source-head alternative isolated by `FD-093` remains outside this mechanism.

## 1. Backward record defect for the complete Schur energy

Fix

\[
\sigma>\frac12
\]

and write

\[
F_\sigma(N):=\frac{E_{N,1}}{N^{2\sigma}}
\qquad(N\ge2).
\tag{1}
\]

For a horizon `H` with `E_(H,1)>0`, define its backward normalized-energy defect by

\[
\boxed{
\mathfrak R_\sigma(H)
:=
\max\!\left\{
1,
\sup_{2\le N<H}
\frac{F_\sigma(N)}{F_\sigma(H)}
\right\}.
}
\tag{2}
\]

Thus `mathfrak R_sigma(H)=1` whenever `H` is a strict or weak record of `F_sigma`, while `mathfrak R_sigma(H)<=K` means that `H` is within a fixed factor `K` of its entire previous normalized-energy maximum.

Suppose a lower physical state `C<H` carries a mask energy `M_C` satisfying

\[
0\le M_C\le E_{C,1}
\]

and, for some `a>0`,

\[
\boxed{
\frac{M_C}{C^{2\sigma}}
\ge (a-o(1))F_\sigma(H).
}
\tag{3}
\]

By the definition of the record defect,

\[
\frac{E_{C,1}}{C^{2\sigma}}
=F_\sigma(C)
\le
\mathfrak R_\sigma(H)F_\sigma(H).
\tag{4}
\]

Dividing (3) by (4) gives the exact composition principle

\[
\boxed{
\frac{M_C}{E_{C,1}}
\ge
\frac{a-o(1)}{\mathfrak R_\sigma(H)}.
}
\tag{5}
\]

If the mask lies in the nonsquarefree sector, `M_C<=U_(C,1)`, then

\[
\boxed{
\frac{U_{C,1}}{E_{C,1}}
\ge
\frac{a-o(1)}{\mathfrak R_\sigma(H)}.
}
\tag{6}
\]

No zero-density estimate, source regularity, or asymptotic formula for the individual lower state is used here. The only input beyond positivity is that the transport theorem and the historical record comparison use the **same normalization exponent**.

## 2. The odd repeated-prime branch becomes fixed occupation at a record

Retain the sharp occupied false-RH packet of `FD-091`, with fixed parent occupation parameter `eta>0`, and suppose the odd-prime alternative occurs. For every fixed `sigma>1/4`, `FD-091` gives a selected odd prime `p` and a lower horizon

\[
C_p=\frac{4H}{p^2}+O(1)
\le\left(\frac49+o(1)\right)H
\]

carrying a nonsquarefree mask `N_(p,H)` such that

\[
\frac{N_{p,H}}{C_p^{2\sigma}}
\ge
\left(a_{\rm odd}(\sigma,\eta)-o(1)\right)
F_\sigma(H),
\tag{7}
\]

where one may take

\[
a_{\rm odd}(\sigma,\eta)
:=
\frac{\eta}
{2\zeta(2)\,4^{2\sigma}\bigl(\zeta(4\sigma)-1\bigr)}
>0.
\tag{8}
\]

For the present record argument we retain `sigma>1/2`, so `C_p<H` and (6) applies directly. Hence

\[
\boxed{
\frac{U_{C_p,1}}{E_{C_p,1}}
\ge
\frac{a_{\rm odd}(\sigma,\eta)-o(1)}
{\mathfrak R_\sigma(H)}.
}
\tag{9}
\]

In particular, if `H` is an `F_sigma` record, then the lower state has a fixed occupation fraction bounded below by `a_odd(sigma,eta)-o(1)`. The composition-strength obstruction left in `FD-091` is therefore **not intrinsic to the odd carrier**; it can only survive there when the parent itself lies increasingly far below an earlier normalized-energy peak.

## 3. Both repairable dyadic alternatives obey the same upgrade

The dyadic branch of `FD-093` has two repairable outcomes before the single head atom is reached.

First, if the already-eligible half-scale part dominates, then with

\[
A=\left\lceil\frac H2\right\rceil
\]

one has

\[
M_{2,H}^{\rm elig}
\le U_{A,1},
\qquad
M_{2,H}^{\rm elig}
\ge\frac\eta4E_{H,1}.
\tag{10}
\]

Therefore

\[
\frac{M_{2,H}^{\rm elig}}{A^{2\sigma}}
\ge
\left(
\frac\eta4\left(\frac HA\right)^{2\sigma}
\right)F_\sigma(H),
\tag{11}
\]

and `H/A=2+o(1)`. Equations (5)--(6) give

\[
\boxed{
\frac{U_{A,1}}{E_{A,1}}
\ge
\frac{\eta\,2^{2\sigma-2}-o(1)}
{\mathfrak R_\sigma(H)}.
}
\tag{12}
\]

Second, if the dyadic terminal mass is nonhead-dominated, `FD-093` produces exact odd-prime repairs satisfying

\[
\sum_pN_{p,H}\ge\frac\eta8E_{H,1},
\qquad
C_p=\frac Hp(1+o(1)),
\qquad
N_{p,H}\le U_{C_p,1}.
\tag{13}
\]

Its prime-weighted normalization states that, for every `sigma>1/2`, some occurring odd prime satisfies

\[
\frac{N_{p,H}}{C_p^{2\sigma}}
\ge
\left(a_{\rm term}(\sigma,\eta)-o(1)\right)
F_\sigma(H),
\tag{14}
\]

with the explicit admissible constant

\[
a_{\rm term}(\sigma,\eta)
:=
\frac{\eta}
{8\bigl(\zeta(2\sigma)-1\bigr)}
>0.
\tag{15}
\]

Since `C_p< H` for all sufficiently large packet horizons,

\[
\boxed{
\frac{U_{C_p,1}}{E_{C_p,1}}
\ge
\frac{a_{\rm term}(\sigma,\eta)-o(1)}
{\mathfrak R_\sigma(H)}.
}
\tag{16}
\]

Thus at an `F_sigma` record, **every nonhead outcome of the current repeated-prime transport already lands in a genuinely lower physical state with fixed nonsquarefree occupation**. No separate mask-versus-state comparison remains to be proved for those branches.

## 4. False RH supplies infinitely many normalized-energy records, but not yet occupied ones

Assume `Theta>1/2` and choose

\[
\frac12<\sigma<\Theta.
\tag{17}
\]

`FD-046` gives the complete Schur-energy frontier

\[
\limsup_{N\to\infty}
\frac{\log(1+E_{N,1})}{\log N}
=2\Theta.
\tag{18}
\]

Consequently

\[
F_\sigma(N)=\frac{E_{N,1}}{N^{2\sigma}}
\]

is unbounded. Hence there are infinitely many strict `F_sigma` record horizons, and on each of them

\[
\mathfrak R_\sigma(H)=1.
\tag{19}
\]

Separately, `FD-083`--`FD-084` provide recurrent near-frontier horizons and polynomial additive blocks with fixed nonsquarefree occupation. What is **not** yet proved is that the two structures intersect with bounded record defect. A set of occupied near-frontier seeds may in principle avoid the strict records of `F_sigma`, and full counting exponent alone does not force an intersection with a sparse record sequence.

This isolates the remaining composition question more sharply. For the repairable channels, it is enough to prove that along some sharp occupied packet sequence

\[
\boxed{
\mathfrak R_\sigma(H)=O(1)
}
\tag{20}
\]

for one fixed `sigma` in `(1/2,Theta)`. Exact recordhood is unnecessary; any bounded backward defect gives a fixed lower-state occupation constant through (9), (12), or (16). Conversely, if every such occupied packet seed has `mathfrak R_sigma(H)->infinity`, then the previously observed vanishing mask fraction is explained by a concrete global phenomenon: the occupied frontier persistently sits below earlier peaks of the normalized complete Schur energy.

## 5. Boundary: the row-two/source-head atom is genuinely separate

The head alternative of `FD-093` is

\[
|\mathcal H(B)|^2
\ge\frac\eta6E_{H,1},
\qquad
B=\frac H4+O(1).
\tag{21}
\]

This is not a lower-state mask inequality of the form (3). The source value `mathcal H(B)` is the excluded row `m=1` after the second dyadic deflation. Preserving that source argument on a nonsquarefree physical row requires the minimal row `4`, which returns to horizon `4B=H+O(1)` rather than a genuine multiplicative predecessor. Therefore the record lemma does not repair the head atom by relabeling it.

The durable frontier is now a clean disjunction. Away from the head atom, the apparent fixed-fraction composition loss disappears whenever the parent occupied frontier has bounded normalized-energy record defect. What remains is either to couple the abundant occupied blocks of `FD-083`--`FD-084` to such near-record horizons, or to show directly that persistent head domination is incompatible with the source dynamics. These are source/global-coherence questions; another round of local prime-weighted normalization cannot decide them.

## 6. Stress tests and prior-art boundary

The normalization in (1) must be the same exponent used by the carrier estimate. Replacing `sigma` by a different exponent after transport inserts a power of `C/H` and destroys the exact record comparison. The condition `C<H` is also essential: a backward record controls only earlier physical horizons. This is why the argument applies immediately to the odd repairs, the half-scale eligible branch, and the dyadic nonhead repairs, but not to the row-two head reembedding at `4B=H+O(1)`.

A bounded record defect is genuinely stronger than the already-known statement that both mask and complete lower energy have exponent `2Theta`. If `mathfrak R_sigma(H)=H^{o(1)}` but tends to infinity, (5) permits precisely the subpower occupation loss left open by `FD-090`--`FD-093`. Thus the present result does not hide the old problem in exponent notation; it identifies the scalar quantity that measures it.

A targeted prior-art audit covered classical Farey discrepancy/Mertens work and GCD/Jordan-matrix literature. Those sources contain the underlying discrepancy and Jordan-totient structures, but no located source states this Mathia-specific normalized-carrier/Schur-energy-record upgrade or the resulting reduction of the recursive composition defect. No external theorem is load-bearing here, so `SOURCES.md` requires no change.

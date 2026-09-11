# MC-213 — Prescribed square-modulus residue has a sharp character-coherence leverage

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `LITERATURE+DERIVED`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-209`--`MC-212` leave one structurally clean escape from the Mertens-complete principal-mode barrier: estimate the **raw source-prescribed residue**

\[
A_d(T)
=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv-q\pmod{d^2}}}\mu(n)
\tag{1}
\]

without bounding its principal and centered pieces separately. The remaining interference can be quantified exactly.

Fix a square-free `d` with `(d,q)=1`, put

\[
\Phi_d:=\varphi(d^2),
\qquad
a_d\equiv-q\pmod{d^2},
\tag{2}
\]

and for every reduced residue `a (mod d^2)` define

\[
A_{d,a}(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv a\pmod{d^2}}}\mu(n).
\tag{3}
\]

As in `MC-210`, write

\[
m_d
:=
\frac{R_{qd}(T)}{\Phi_d},
\qquad
R_{qd}(T)
:=
\sum_{\substack{n\le T\\(n,qd)=1}}\mu(n),
\tag{4}
\]

and

\[
E_{d,a}:=A_{d,a}(T)-m_d,
\qquad
\sum_a^*E_{d,a}=0.
\tag{5}
\]

Thus the raw coefficient is

\[
A_d(T)=m_d+E_{d,a_d}.
\tag{6}
\]

Define the **normalized full-residue centered energy**

\[
\boxed{
B_d
:=
\frac1{\Phi_d}\sum_a^*|E_{d,a}|^2.
}
\tag{7}
\]

Then the distinguished coordinate satisfies the sharp inequality

\[
\boxed{
|E_{d,a_d}|^2
\le
(\Phi_d-1)B_d.
}
\tag{8}
\]

The factor `\Phi_d-1` is optimal in the ambient zero-sum residue space. For any complex number `z`, equality in `(8)` is attained by

\[
E_{d,a_d}=z,
\qquad
E_{d,a}=-\frac{z}{\Phi_d-1}
\quad(a\ne a_d).
\tag{9}
\]

Consequently a single prescribed centered residue can be `sqrt(\Phi_d-1)` times its residue-class RMS. Since the active root moduli are `y`-rough with `y=c\log X`, one has uniformly

\[
\Phi_d=d^2(1+o(1)),
\tag{10}
\]

so the amplitude leverage is of order `d`, and the energy leverage is of order `d^2`.

This has two immediate consequences for the live square-defect route.

First, **diagonal-scale all-residue centered variance does not by itself give diagonal-scale control of the source-prescribed centered coordinate.** On a dyadic root shell let

\[
\mathcal B_D
:=
\sum_{\substack{D<d\le2D\\(d,q)=1}}
 d\mu^2(d)B_d,
\tag{11}
\]

and retain the selected-residue centered energy of `MC-210`,

\[
Z_D
:=
\sum_{\substack{D<d\le2D\\(d,q)=1}}
 d\mu^2(d)|E_{d,a_d}|^2.
\tag{12}
\]

Then `(8)` gives

\[
\boxed{
Z_D
\le
\max_{D<d\le2D}(\Phi_d-1)\,\mathcal B_D
\ll D^2\mathcal B_D.
}
\tag{13}
\]

The `D^2` loss is sharp up to the harmless `1+o(1)` totient factor for unrestricted zero-sum residue profiles. Yet the literal `n=m` contribution to the normalized all-residue energy `(11)` already has the natural shell scale

\[
\sum_{D<d\le2D}
\frac d{\Phi_d}
\sum_{\substack{n\le T\\(n,qd)=1}}\mu^2(n)
\ll
X\sum_{D<d\le2D}\frac1d
\ll X.
\tag{14}
\]

Thus an all-residue BDH-type estimate at its natural `X^{1+o(1)}` scale can still give only `Z_D\ll D^2X^{1+o(1)}` through generic Hilbert-space control. Recovering the `Z_D\ll X^{1+o(1)}` scale by this route would require a further `D^{-2}` anti-concentration gain showing that the source-selected residue is typical rather than potentially exceptional.

Second, **if the principal mode is large while the raw energy remains small, the escape requires quantitative anti-alignment, not merely transverse variance.** Define

\[
P_D
:=
\sum_d d\mu^2(d)|m_d|^2,
\qquad
W_D
:=
\sum_d d\mu^2(d)|m_d+E_{d,a_d}|^2,
\tag{15}
\]

with the same dyadic restrictions as above, and

\[
I_D
:=
\sum_d d\mu^2(d)
\operatorname{Re}\!\left(m_d\overline{E_{d,a_d}}\right).
\tag{16}
\]

Then exactly

\[
\boxed{
W_D=P_D+Z_D+2I_D.
}
\tag{17}
\]

If for some `0<eta<1`

\[
W_D\le\eta P_D,
\tag{18}
\]

then, regarding `\sqrt d\,\mu^2(d)^{1/2}m_d` and `\sqrt d\,\mu^2(d)^{1/2}E_{d,a_d}` as vectors over the shell,

\[
\boxed{
\|E+M\|_2
\le
\sqrt\eta\,\|M\|_2,
}
\tag{19}
\]

and hence

\[
\boxed{
|\sqrt{Z_D}-\sqrt{P_D}|
\le
\sqrt{\eta P_D}.
}
\tag{20}
\]

So whenever a super-diagonal principal contribution is rescued by a diagonal-scale raw bound, the selected centered vector must be nearly the **negative** of the principal vector in weighted `ell^2`; magnitude control alone is insufficient.

The character expansion makes the missing information explicit. For Dirichlet characters on

\[
G_d=(\mathbb Z/d^2\mathbb Z)^\times
\tag{21}
\]

put

\[
S_d(\chi)
:=
\sum_{a\in G_d}A_{d,a}(T)\overline{\chi(a)}.
\tag{22}
\]

Then `S_d(1)=R_{qd}(T)` and Fourier inversion gives

\[
\boxed{
E_{d,a_d}
=
\frac1{\Phi_d}
\sum_{\chi\ne1}S_d(\chi)\chi(a_d),
}
\tag{23}
\]

while Parseval gives

\[
\boxed{
B_d
=
\frac1{\Phi_d^2}
\sum_{\chi\ne1}|S_d(\chi)|^2.
}
\tag{24}
\]

Inequality `(8)` is exactly Cauchy--Schwarz applied to `(23)`. Equality means that the complete nonprincipal character vector is aligned with the evaluation phase vector `\overline{\chi(a_d)}`. Therefore the unresolved interference in `(17)` is a **directed character-coherence problem at the source-prescribed residue**, not merely a problem of bounding the total transverse character energy.

This is the mathematical delta beyond `MC-210`--`MC-212`: standard centering exposed the Mertens-complete principal mode, but the raw route survives because the chosen residue breaks unit-group translation symmetry and permits coherent principal/transverse interference. The price of that escape is now exact. A proof using only an all-residue `L^2`/large-sieve/BDH magnitude bound loses a factor of order `d^2` when it asks about the one source-selected residue; a proof using interference must control the **phase and sign** of `(23)` relative to `R_{qd}(T)`, strongly enough to make `(19)` hold whenever separate principal control would be too expensive.

No estimate for `W_D`, `Z_D`, `P_D`, `M(X)`, or any zeta zero-free region is proved here.

## 1. Sharp point-evaluation inequality

Fix `d` and abbreviate `\Phi=\Phi_d`, `E_a=E_{d,a}` and `a_0=a_d`. Since `\sum_aE_a=0`,

\[
\sum_{a\ne a_0}E_a=-E_{a_0}.
\tag{25}
\]

Cauchy--Schwarz gives

\[
|E_{a_0}|^2
\le
(\Phi-1)
\sum_{a\ne a_0}|E_a|^2.
\tag{26}
\]

Equivalently,

\[
\sum_a|E_a|^2
\ge
\frac{\Phi}{\Phi-1}|E_{a_0}|^2.
\tag{27}
\]

Dividing by `\Phi` proves `(8)`. Equality in `(26)` holds exactly when all `E_a`, `a\ne a_0`, are equal, which gives `(9)` and proves sharpness.

This also gives a useful compensation threshold. If the raw prescribed coefficient vanishes, `A_d(T)=0`, then `E_{d,a_d}=-m_d`, and every centered residue profile capable of that cancellation must satisfy

\[
\boxed{
B_d
\ge
\frac{|m_d|^2}{\Phi_d-1}.
}
\tag{28}
\]

The bound is sharp in the ambient residue space. More generally, if

\[
|A_d(T)|\le\eta|m_d|
\qquad(0\le\eta<1),
\tag{29}
\]

then the reverse triangle inequality gives

\[
|E_{d,a_d}|\ge(1-\eta)|m_d|
\tag{30}
\]

and therefore

\[
\boxed{
B_d
\ge
\frac{(1-\eta)^2|m_d|^2}{\Phi_d-1}.
}
\tag{31}
\]

Because `\Phi_d\asymp d^2`, the full-residue RMS budget needed to cancel a large mean at **one** residue is smaller than the mean-square size by a factor of order `d^2`. This is why a global transverse-variance estimate can coexist with strong cancellation at one selected residue without contradiction.

## 2. The natural all-residue diagonal scale does not remove the leverage

The full-residue square expansion is

\[
\sum_a^*|A_{d,a}(T)|^2
=
\sum_{\substack{n_1,n_2\le T\\(n_1n_2,q)=1\\n_1\equiv n_2\pmod{d^2}}}
\mu(n_1)\mu(n_2),
\tag{32}
\]

where reduced residues automatically impose `(n_1n_2,d)=1`. The literal diagonal `n_1=n_2` contributes at most `X`. Since

\[
\sum_a^*|E_{d,a}|^2
=
\sum_a^*|A_{d,a}|^2
-
\Phi_d|m_d|^2,
\tag{33}
\]

the normalization in `(7)` turns the per-modulus diagonal scale into `O(X/\Phi_d)`. Weighting by `d` and summing `d\asymp D` gives `(14)` because `d/\Phi_d\asymp1/d`.

This calibration is important. The factor `D^2` in `(13)` is not caused by choosing an unnaturally large normalization for `\mathcal B_D`; it is exactly the cost of passing from an RMS statement over about `d^2` reduced residues to one distinguished coordinate without any source-specific anti-concentration theorem.

The same fact is transparent in character space. Equations `(23)`--`(24)` say that the all-residue variance knows the Euclidean norm of the nonprincipal character vector, while the prescribed residue asks for its inner product with one phase vector of squared norm `\Phi_d-1`. Large-sieve and BDH bounds are naturally norm bounds. They do not, by themselves, determine whether that vector is aligned, orthogonal, or anti-aligned with the source-selected evaluation direction.

## 3. Interference escape is a phase theorem

Equation `(17)` separates three logically different objects:

- `P_D`, the principal energy shown in `MC-210`--`MC-212` to be Mertens-complete under broad separate-control hypotheses;
- `Z_D`, the magnitude of the centered component at the one source-prescribed residue;
- `I_D`, their signed covariance.

The inequality `W_D\le2P_D+2Z_D` used in `MC-210` discards `I_D`. That loss was known qualitatively. Equations `(8)`, `(13)` and `(19)` identify what recovering it entails.

If `P_D` is already at diagonal scale, no special interference is needed. The interesting regime is precisely `P_D\gg X^{1+o(1)}` while one hopes for `W_D\ll X^{1+o(1)}`. In that regime `(19)` says that the selected transverse vector must track `-M` with relative weighted `ell^2` error `O((W_D/P_D)^{1/2})`. It is therefore not enough to prove that transverse coefficients are collectively small, pseudorandom, equidistributed, or of the expected second-moment size. One needs a theorem tying their **directed source phase** `(23)` to the sign and size of the rough principal coefficient `(4)`.

This does not make the route impossible. The residue `a_d=-q` is not arbitrary: it comes from the exact square-defect identity, so an arithmetic mechanism could in principle force precisely such alignment. But that mechanism would be new input relative to ordinary centered variance. Conversely, a proposed proof which replaces `(23)` by Cauchy--Schwarz and then inserts a full-residue variance theorem has paid the sharp `d^2` leverage tax and has not used the source-specific interference.

## 4. Relation to the earlier no-go results

This finding does not duplicate `MC-190` or `MC-191`. Those results concern unit-group-equivariant linear/Hermitian quadratic statistics and natural equivariant transport between nested moduli. Such operators diagonalize in character sectors and cannot create principal/nonprincipal cross terms.

Here the observable is **evaluation at one distinguished residue** `a_d=-q`. Point evaluation is not invariant under multiplicative translation; it explicitly chooses a source-anchored direction. It therefore evades the equivariant diagonalization no-go exactly as the live `MC-210` escape requires. Equation `(23)` shows how: all nonprincipal characters are recombined with phases depending on the chosen residue.

Nor does the result duplicate `MC-199`. That finding proves that centered residue data alone cannot reconstruct the deleted principal coordinate. The present result asks a different question: once the principal coordinate and the complete centered profile coexist inside the raw prescribed coefficient, how much centered energy is needed to cancel the principal value at that one coordinate, and what information is lost by replacing the directed evaluation with an all-residue norm? The sharp answer is `(8)`--`(13)`.

## 5. Prior-art audit

The finite-dimensional inequalities `(8)` and `(27)` are elementary zero-sum Hilbert-space geometry, and `(23)`--`(24)` are ordinary finite-abelian-group Fourier inversion and Parseval. No novelty is claimed for those mechanisms.

Adam J. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences* (Journal of the London Mathematical Society 112 (2025), e70293; DOI `10.1112/jlms.70293`), studies centered progression variance for general sequences. As already audited in `MC-210`, this is an all-residue centered magnitude framework: it controls a quadratic norm after the appropriate class average has been removed. It does not by itself supply the directed phase correlation `(16)` or turn an RMS residue estimate into a sharp estimate for the single source-selected residue without the leverage in `(8)`.

Baier and Zhao, *Bombieri--Vinogradov type theorems for sparse sets of moduli* (Acta Arithmetica 125 (2006), 187--201), and the square-modulus large-sieve literature audited in `MC-209` establish that substantial mean-square averaging is possible over square moduli. Stephan Baier, *The Large Sieve for Square Moduli, Revisited* (Hardy--Ramanujan Journal 48 (2025), published 2026; DOI `10.46298/hrj.2026.17906`), further analyzes square-modulus large-sieve norms and conditional improvements from additive-energy information. These are norm/mean-square controls over families of residue or Fourier directions; they do not provide the principal/transverse sign relation in `(17)`.

Linnik's dispersion method and its descendants can attack fixed or source-specified residue problems when additional bilinear/exponential-sum structure is available. That is a potentially relevant positive route rather than a counterexample to the present obstruction: a successful dispersion argument for `(1)` would be using extra arithmetic structure to estimate the raw selected residue directly, instead of deducing it from an all-residue `L^2` bound alone.

Keating and Rudnick (`MC-S44`) calculate Möbius progression variances in the function-field analogue, and Klurman--Mangerel--Teräväinen (`MC-S45`) provide strong smooth-modulus centered dispersion for multiplicative functions. They reinforce the naturality of transverse variance but do not remove the selected-coordinate leverage or prove the source-phase coupling required here.

A targeted search over square-modulus large sieve, general-sequence BDH, fixed-residue dispersion, and Möbius arithmetic-progressions literature found no theorem used here as evidence for a Möbius-specific anti-alignment of the form `(19)` for the growing primorial/square-defect family. This is not a literature-absence or novelty claim.

## 6. Boundaries and falsification tests

- The sharp profiles `(9)` are abstract zero-sum residue vectors. They are not asserted to be realizable by Möbius progression sums. Their role is to prove that **generic centered `L^2` information alone** cannot improve the factor in `(8)`; Möbius-specific arithmetic restrictions may do better.
- The finding does not prove that `P_D` is large, that `W_D` is small, or that the required anti-alignment actually occurs. It identifies the exact structure a successful interference proof must control.
- A theorem giving an `L^infinity` residue bound, sufficiently high moments, a source-specific anti-concentration theorem, or a direct dispersion estimate for `a_d=-q` can evade `(13)`. Such a theorem would be additional input beyond a standard all-residue second moment.
- The `D^2` leverage is a polynomial obstruction only on polynomial root-modulus scales. For `D=X^{o(1)}` it is itself subpower and may be absorbable; this does not remove the intermediate-shell problem exposed by `MC-209`.
- The estimate `\Phi_d=d^2(1+o(1))` uses the active `y`-rough condition. Without it, the exact statements remain `(8)` and `(13)` with `\Phi_d` in place of `d^2`.
- The diagonal calibration `(14)` is not a proof that `\mathcal B_D\ll X^{1+o(1)}`: off-diagonal correlations remain. It only shows that the normalization of `\mathcal B_D` has the same natural literal-diagonal scale as the raw target.
- Negative interference is useful here, not pathological. The obstruction is only to proving that interference from magnitude-only variance information; a source identity that forces the phase relation would be a genuine mechanism.
- No RH implication is claimed beyond the conditional relationships already established in `MC-209`--`MC-212`.

## Consequence for the line

After `MC-212`, the square-defect branch should no longer ask generically for “a better centered variance theorem.” There are now two quantitatively distinct theorem surfaces.

One is a **direct raw prescribed-residue estimate** for `W_D`, potentially via a dispersion/bilinear mechanism that never separates the principal mode. The other is a **directed coherence theorem** showing that the nonprincipal character combination `(23)` anti-aligns with `R_{qd}(T)/\Phi_d` on exactly the shells where the separate principal energy is too large. Ordinary all-residue BDH or square-modulus large-sieve magnitude estimates do not supply either surface by themselves.

That distinction keeps the surviving route non-circular and gives a cheap falsification test for future candidates: if a proposed argument reaches the prescribed residue only by Cauchy--Schwarz from a centered all-residue `L^2` norm, it must explicitly pay the sharp `d^2` leverage in `(13)`; if it claims to exploit interference, it must exhibit arithmetic control of the signed covariance `I_D` or an equivalent source-phase quantity.
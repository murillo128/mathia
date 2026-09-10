# MC-191 — Natural nested-primorial transport remains character-sector diagonal

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-188` isolates the current rough Möbius obstruction at one logarithmic primorial: strong signed dispersion controls the nonprincipal character directions, while the principal character coefficient is the rough global sum. `MC-190` then shows that no translation-invariant linear or Hermitian quadratic statistic on that single residue vector can mix the principal direction with the transverse characters.

A natural possible escape left open there is to use **several nested primorial moduli**. The extra restriction/lifting data are real, but the canonical Chinese-remainder bonding maps still do not provide the missing coupling. In fact, both the abstract equivariant transport and the exact Möbius recursion across nested rough cutoffs remain character-sector diagonal.

Let `q` and `r` be coprime square-free integers, put

\[
Q=qr,
\qquad
G_q=(\mathbb Z/q\mathbb Z)^\times,
\qquad
G_Q=(\mathbb Z/Q\mathbb Z)^\times,
\]

and let

\[
\pi:G_Q\to G_q
\]

be reduction modulo `q`. For `b` in either unit group write

\[
(\tau_bF)(a)=F(b^{-1}a).
\]

Then every linear map

\[
T:L^2(G_Q)\to L^2(G_q)
\]

that intertwines the natural quotient actions,

\[
T\tau_b=\tau_{\pi(b)}T
\qquad(b\in G_Q),
\tag{1}
\]

has the following exact character-selection rule. If `psi` is a character of `G_Q`, then

\[
\boxed{
T\psi=0
\quad\text{unless}\quad
\psi=\chi\circ\pi
\text{ for a unique }\chi\in\widehat G_q,
}
\tag{2}
\]

and in the surviving case

\[
\boxed{T(\chi\circ\pi)=c_\chi\chi}
\tag{3}
\]

for some scalar `c_chi`. In particular, the principal character can map only to the principal character. No equivariant linear bonding map can turn a nonprincipal fine-modulus character into the coarse principal mode or conversely.

The actual Möbius residue vectors satisfy a stronger arithmetic identity of exactly this sector-preserving form. Define

\[
A_q(X;a)
=
\sum_{\substack{n\le X\\n\equiv a\pmod q}}\mu(n),
\qquad a\in G_q,
\tag{4}
\]

and analogously `A_Q`. Let the fiber-sum pushforward be

\[
(RF)(a)
=
\sum_{\substack{b\in G_Q\\\pi(b)=a}}F(b).
\tag{5}
\]

Then for every real `X>=1`,

\[
\boxed{
A_q(X)
=
\sum_{d\mid r}\mu(d)\,\tau_d\,R A_Q(X/d).
}
\tag{6}
\]

With normalized Fourier coefficients

\[
\widehat F_q(\chi)
=
\frac1{\varphi(q)}
\sum_{a\in G_q}F(a)\overline{\chi(a)},
\tag{7}
\]

and with the inflated character `\widetilde\chi=\chi\circ\pi`, equation `(6)` becomes

\[
\boxed{
\widehat A_q(X;\chi)
=
\varphi(r)
\sum_{d\mid r}
\mu(d)\overline{\chi(d)}
\widehat A_Q(X/d;\widetilde\chi).
}
\tag{8}
\]

Every coarse character therefore depends only on its **same lifted character sector** at the finer modulus, evaluated at the finitely many scales `X/d`. There is no principal/nonprincipal term in `(8)`.

For the principal character this reduces to the exact rough-sum recursion

\[
\boxed{
G_q(X)
=
\sum_{d\mid r}\mu(d)G_Q(X/d),
}
\tag{9}
\]

where

\[
G_q(X)=\sum_{\substack{n\le X\\(n,q)=1}}\mu(n).
\tag{10}
\]

At the active nested primorials `q=q_y=\prod_{p\le y}p` and `Q=q_z=\prod_{p\le z}p` with `z>y`, `(10)` is exactly the logarithmically rough Möbius zero mode from `MC-180`--`MC-190`. Equation `(9)` says that natural cutoff refinement relates a coarse rough zero mode only to **finer rough zero modes**. It does not convert transverse character cancellation into principal cancellation.

Consequently the cross-modulus escape left open by `MC-190` can now be narrowed: **merely replacing one primorial by a nested tower, while transporting data through the natural quotient/pushforward/pullback maps and Möbius inclusion-exclusion, does not break the character diagonalization.** A successful multiscale mechanism must add structure not contained in this equivariant bonding system.

## 1. Quotient-equivariant maps cannot mix character sectors

The proof of `(2)`--`(3)` is elementary finite-group representation theory.

Let `psi` be a character of `G_Q`. If `k` lies in the kernel of `pi`, then the action on the target satisfies

\[
\tau_{\pi(k)}=I.
\]

Using `(1)` and

\[
\tau_k\psi=\overline{\psi(k)}\psi,
\]

we obtain

\[
T\psi
=T\tau_k\psi
=\overline{\psi(k)}T\psi.
\tag{11}
\]

If `psi` is nontrivial on `ker(pi)`, choose `k` with `psi(k)\ne1`; then `(11)` forces `T\psi=0`.

If `psi` is trivial on `ker(pi)`, it factors uniquely through the quotient:

\[
\psi=\chi\circ\pi
\]

for one character `chi` of `G_q`. For every `b\in G_Q`,

\[
\tau_{\pi(b)}(T\psi)
=T(\tau_b\psi)
=\overline{\chi(\pi(b))}\,T\psi.
\tag{12}
\]

Thus `T\psi` lies in the `chi`-eigenspace of the regular representation of `G_q`. Since `G_q` is finite abelian, that eigenspace is one-dimensional and spanned by `chi`, proving `(3)`.

In particular, the fine principal character is inflated from the coarse principal character and cannot be sent to any other sector. Fine characters that oscillate along the fibers of `pi` are annihilated by every quotient-equivariant map into `L^2(G_q)`.

The standard pushforward `(5)` is such an intertwiner. Its adjoint pullback `PF=F\circ\pi` is likewise sector preserving in the opposite direction. Translation-invariant convolution operators at either level are already diagonal by `MC-190`. Therefore arbitrary linear compositions of these canonical operations still preserve character labels.

## 2. Exact Möbius inclusion-exclusion across a new prime block

Fix `a\in G_q`. Since `n\equiv a (mod q)` implies `(n,q)=1`, partition the nonzero Möbius terms in `(4)` according to

\[
d=(n,r).
\]

Because `r` is square-free and `\mu(n)\ne0`, every such `d` is a divisor of `r`. Write `n=dm`. Then

\[
(m,Q)=1,
\qquad
\mu(n)=\mu(d)\mu(m),
\qquad
m\equiv d^{-1}a\pmod q.
\tag{13}
\]

Conversely, for every `d|r` and every square-free contributing `m` with `(m,Q)=1`, `m<=X/d`, and `m\equiv d^{-1}a (mod q)`, the integer `n=dm` contributes exactly once to `(4)`. Terms with `\mu(n)=0` contribute nothing on either side.

Hence

\[
A_q(X;a)
=
\sum_{d\mid r}\mu(d)
\sum_{\substack{m\le X/d\\(m,Q)=1\\m\equiv d^{-1}a\pmod q}}
\mu(m).
\tag{14}
\]

For fixed `d`, the inner sum is obtained by summing `A_Q(X/d;b)` over all unit classes `b (mod Q)` that reduce to `d^{-1}a (mod q)`. This is exactly

\[
(\tau_d R A_Q(X/d))(a),
\]

which proves `(6)`.

For one newly inserted prime `p\nmid q`, `(6)` has the particularly transparent form

\[
\boxed{
A_q(X)
=
R A_{qp}(X)
-
\tau_p R A_{qp}(X/p).
}
\tag{15}
\]

The second term remembers that integers counted at level `q` but absent from the unit classes modulo `qp` are exactly those carrying the new prime `p`. The correction is arithmetic, but it is still a translation inside the same coarse character sector.

## 3. Fourier transport is exactly diagonal across the refinement

The fiber of `pi` has cardinality `varphi(r)`. For `chi\in\widehat G_q`, direct substitution in `(5)` gives

\[
\widehat{RF}_q(\chi)
=
\frac1{\varphi(q)}
\sum_{b\in G_Q}F(b)\overline{\chi(\pi(b))}
=
\varphi(r)\widehat F_Q(\widetilde\chi).
\tag{16}
\]

Also

\[
\widehat{\tau_d F}_q(\chi)
=
\overline{\chi(d)}\widehat F_q(\chi),
\tag{17}
\]

because `d` is coprime to `q`. Applying `(16)`--`(17)` to `(6)` proves `(8)`.

For `chi=1`, normalized Fourier coefficients satisfy

\[
\widehat A_q(X;1)=\frac{G_q(X)}{\varphi(q)},
\qquad
\widehat A_Q(X;1)=\frac{G_Q(X)}{\varphi(Q)}.
\]

Since `varphi(Q)=varphi(q)varphi(r)`, equation `(8)` gives `(9)` exactly.

This is the important point for the current frontier: the extra scale values `X/d` do not themselves mix representations. They change the **radial/size parameter** of the fine vector while leaving its character label unchanged. A family estimate for nonprincipal `\widetilde\chi` therefore remains nonprincipal information after exact cutoff refinement.

## 4. Cross-level quadratic statistics do not evade the obstruction either

Suppose a cross-level bilinear statistic uses an equivariant map `T` as in `(1)`, for example

\[
B(F_q,F_Q)=\langle F_q,TF_Q\rangle_{G_q}.
\tag{18}
\]

By `(2)`--`(3)`, its Fourier expansion pairs `\widehat F_q(\chi)` only with the coefficient of the inflated fine character `\chi\circ\pi`. Thus its principal contribution pairs principal with principal, and every nonprincipal contribution remains in its matching nonprincipal sector.

This covers the most immediate attempt to evade `MC-190` by replacing a same-modulus covariance with a covariance between adjacent primorial levels. If the cross-level kernel is compatible with the quotient symmetry, representation theory again diagonalizes it before any Möbius estimate enters.

Likewise, summing such diagonal energies over many nested primorials does not produce an off-diagonal coupling. It merely accumulates separate estimates for the same character chains through the tower.

This does **not** rule out all multiscale statistics. It rules out the canonical equivariant linear/bilinear category in which the only new information is restriction, lifting, fiber summation, group convolution, translation, and scale change.

## 5. Consequence for the active rough-parity frontier

Take

\[
q_y=\prod_{p\le y}p,
\qquad
q_z=\prod_{p\le z}p,
\qquad
r_{y,z}=q_z/q_y.
\]

Then the principal coefficient of `A_{q_y}` is the rough sum

\[
G_y(X)=\sum_{\substack{n\le X\\P^-(n)>y}}\mu(n),
\]

and `(9)` becomes

\[
\boxed{
G_y(X)
=
\sum_{d\mid r_{y,z}}\mu(d)G_z(X/d).
}
\tag{19}
\]

This identity is useful bookkeeping, but it exposes rather than solves the fixed-power barrier. `MC-187` already shows that each logarithmically rough zero mode inherits the classical Korobov--Vinogradov subpower scale. Equation `(19)` does not inject any transverse information capable of upgrading that scale: it is a relation entirely inside the principal chain.

Meanwhile the nonprincipal recursion `(8)` may transport strong dispersion information from `MC-188` through the tower, but those coefficients never enter `(19)`. Hence a proof that merely obtains better control of more nonprincipal characters at more primorial levels is still missing the same resource.

The nested-modulus option left open in `MC-190` therefore survives only in a narrower form. A genuine escape must do at least one of the following:

- use a **source-forced non-equivariant operator**, for example one tied quantitatively to the ordered interval boundary rather than only to unit-group structure;
- exploit a **nonlinear arithmetic interaction** whose character product can land in the principal sector, rather than a linear or Hermitian-quadratic intertwiner;
- construct a cross-scale relation carrying additional arithmetic data not recoverable from the canonical CRT bonding maps;
- or supply an independently controlled fixed-power principal term.

The second possibility is structurally real: products of nonprincipal characters can have trivial total character, for example `chi * conjugate(chi)=1`. But that observation alone gives no useful inequality; a successful nonlinear route must prove a source-side estimate that turns such representation-theoretic compatibility into fixed-power control of `G_y`.

## 6. Prior art and novelty audit

The representation-theoretic content of `(2)`--`(3)` is standard. Characters diagonalize the regular representation of a finite abelian group, and quotient maps identify characters of the quotient with characters upstairs that are trivial on the kernel. The finite-group Fourier framework is covered, for example, by Audrey Terras, *Fourier Analysis on Finite Groups and Applications*, Cambridge University Press, London Mathematical Society Student Texts 43 (1999), especially Part I and the finite-abelian DFT treatment; Cambridge DOI `10.1017/CBO9780511626265`. Induction/restriction and character transport are likewise standard finite representation theory. No novelty is claimed for these facts.

The arithmetic decomposition `(6)` is elementary Möbius inclusion-exclusion across a disjoint prime block. It is in the same classical Euler-factor family as the cutoff convolution already used in `MC-180`; no novelty is claimed for prime-block splitting or the principal recursion `(9)` as standalone identities. Rough Möbius sums themselves are established prior art in the Alladi/Hazlewood literature already audited in `MC-180` and `SOURCES.md`.

A targeted literature search for finite-abelian Fourier transport under quotients and for recursive Möbius summatory identities found the standard representation/character machinery and general Möbius recursions, but no reason to present `(2)`--`(9)` as a new theorem of analytic number theory. The durable Mathia contribution is instead the **frontier classification**: the exact natural bonding structure of the nested primorial tower lies inside the same character-sector-preserving category that `MC-190` identified at one modulus. Thus one specific proposed escape from the zero-mode obstruction is narrowed without claiming novelty for the ingredients.

## 7. Boundaries and falsification tests

- The result concerns square-free coprime prime blocks, exactly the setting of nested primorials. It does not classify arbitrary changes of modulus with shared prime powers or noncanonical correspondences.
- Equation `(2)` applies to **linear quotient-equivariant** maps. A deliberately non-equivariant boundary operator is outside the theorem; its arithmetic naturalness and the size of its symmetry-breaking term must be proved rather than assumed.
- Equation `(18)` covers bilinear/quadratic cross-level statistics whose transport is equivariant. Higher-degree nonlinear statistics are not ruled out.
- The recursion `(6)` uses the actual cutoff dependence of Möbius and is exact. It does not assert that knowing `A_Q` at finitely many scaled endpoints is analytically easier than knowing `A_q`; it only classifies the character sectors involved.
- Fine characters nontrivial on `ker(pi)` are invisible under canonical pushforward, but they could participate in a nonlinear invariant before pushforward. Such a route contains information absent from `(6)` and is not excluded.
- Summing or averaging diagonal identities over a tower remains diagonal. A proposed multiscale escape must exhibit the exact operation that breaks this statement rather than appeal only to the existence of many scales.
- The principal recursion `(19)` is not itself a Mertens improvement. Any fixed-power conclusion still requires fixed-power input somewhere in the principal chain or a genuinely new coupling.

The finding would fail as a no-go for a proposed nested-primorial route if that route produced a principal/nonprincipal coupling using only quotient-equivariant linear transport, canonical CRT pushforward/pullback, translations, and Hermitian quadratic pairing. Equations `(2)`--`(3)` forbid such a coupling. A route that adds a nonlinear or source-forced non-equivariant ingredient is outside the claim and remains a legitimate next target.

## Consequence for the line

The immediate instruction after `MC-190` was to test whether relations between several primorial groups add information absent at one scale. The answer is now sharper: **the canonical nested-group relations do add refinement data, but not cross-character information**. Their exact Möbius inclusion-exclusion stays inside the principal chain for the zero mode and inside matching lifted chains for every transverse character.

The next useful investigation should therefore stop treating generic nested-modulus covariance or CRT refinement as an unexplored bridge. The surviving multiscale question is whether Möbius supplies a mathematically forced **nonlinear or boundary-sensitive coupling** that is not an equivariant intertwiner and that can cross the fixed-power zero-mode budget identified in `MC-185`--`MC-187`.
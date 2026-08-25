# Prime-circle findings

## PC-001 — the common-vertex potential is exactly von Mangoldt

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE` (geometric organization)

Let

\[
P_n^*=\{\zeta:\operatorname{ord}(\zeta)=n\}
\]

be the vertices that appear for the first time in the regular \(n\)-gon. Define their dimensionless logarithmic chord potential at the common vertex \(1\) by

\[
E_n:=\sum_{\zeta\in P_n^*}\log|1-\zeta|.
\]

Since

\[
\Phi_n(x)=\prod_{\zeta\in P_n^*}(x-\zeta),
\]

we have exactly

\[
E_n=\log|\Phi_n(1)|.
\]

For \(n>1\), the classical cyclotomic identity

\[
\Phi_n(1)=e^{\Lambda(n)}
\]

therefore gives

\[
\boxed{E_n=\Lambda(n).}
\]

Equivalently,

\[
E_n=\begin{cases}
\log p,&n=p^k,\\
0,&\text{otherwise.}
\end{cases}
\]

Thus the von Mangoldt source strength is not inserted into the original construction: it is the exact total logarithmic chord interaction between the common vertex and the new-vertex shell at level \(n\).

The Mellin/Dirichlet transform

\[
\sum_{n\ge2}E_n n^{-s}=-\frac{\zeta'(s)}{\zeta(s)}
\]

is classical and should **not** by itself be counted as a new RH mechanism. The potentially useful new direction is to retain the full two-dimensional potential field before taking this scalar transform.

### Literature check

The identity \(\Phi_n(1)=e^{\Lambda(n)}\) is classical and is explicitly discussed in Bzdęga–Herrera-Poyatos–Moree, *Cyclotomic polynomials at roots of unity*. The geometric logarithmic-chord interpretation is immediate from the defining product for \(\Phi_n\); novelty is not claimed for the identity.

---

## PC-002 — pairwise primitive-shell interaction detects prime-power scale jumps

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE`

For distinct primitive layers \(m<n\), define the total logarithmic interaction

\[
I_{m,n}:=
\sum_{\zeta\in P_m^*}
\sum_{\eta\in P_n^*}
\log|\zeta-\eta|.
\]

By the defining formula for the polynomial resultant,

\[
I_{m,n}=\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
\]

Apostol's classical resultant theorem gives, for \(n>m>1\),

\[
|\operatorname{Res}(\Phi_m,\Phi_n)|
=
\begin{cases}
p^{\varphi(m)},&n/m=p^k\text{ for a prime }p,\\
1,&\text{otherwise.}
\end{cases}
\]

Hence

\[
\boxed{
I_{m,n}
=
\varphi(m)\,\Lambda(n/m)
}
\]

when \(m\mid n\), and \(I_{m,n}=0\) otherwise.

After normalization by the number of charges in the lower shell,

\[
\boxed{
\frac{I_{m,n}}{\varphi(m)}
=
\Lambda(n/m).
}
\]

So the original circle carries a canonical interaction graph on primitive layers in which nonzero couplings occur exactly across prime-power multiplicative jumps.

This suggests studying the **full interaction operator/geometry** before diagonalizing it by a Dirichlet transform. Immediately replacing it by \(-\zeta'/\zeta\) would only restate known arithmetic.

### Literature check

The resultant formula is classical: T. M. Apostol, *Resultants of cyclotomic polynomials*, Proc. AMS 24 (1970), 457–462. Later proofs and extensions exist. No novelty is claimed for the resultant itself.

---

## PC-003 — exact harmonic interior/exterior duality of primitive-shell potentials

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`

Define the logarithmic potential of the primitive layer

\[
U_n(z)=\log|\Phi_n(z)|
=\sum_{\zeta\in P_n^*}\log|z-\zeta|,
\qquad n>1.
\]

Away from the unit circle charges, \(U_n\) is harmonic. Cyclotomic reciprocity gives

\[
\Phi_n(z)=z^{\varphi(n)}\Phi_n(1/z),
\qquad n>1,
\]

and therefore, in modulus,

\[
\boxed{
U_n(z)
=
\varphi(n)\log|z|
+U_n(1/\bar z).
}
\]

Thus inversion in the original circle gives an **intrinsic exact inside/outside relation for the potential field**. Unlike the prime-flute interior/exterior picture, this duality belongs directly to the original roots-of-unity object.

At the common boundary vertex,

\[
U_n(1)=\Lambda(n),
\]

by PC-001.

The full polygon potential and primitive-shell potential are related by exact divisor/Möbius decomposition:

\[
\log|z^n-1|
=
\sum_{d\mid n}U_d(z),
\]

and formally away from singularities,

\[
\boxed{
U_n(z)
=
\sum_{d\mid n}\mu(n/d)\log|z^d-1|.
}
\]

This is currently the most promising original-geometry object: a two-sided harmonic field whose boundary charges are the genuinely new polygon vertices, whose common-vertex source strength is von Mangoldt, and whose inter-layer energies are cyclotomic resultants.

### Research gate

Do **not** count a Mellin transform of \(U_n(1)=\Lambda(n)\) as progress; that immediately recovers the classical logarithmic derivative of \(\zeta\). A substantive next step must use information in the full field \(U_n(z)\), its interior/exterior coupling, its Fourier/Ramanujan modes, or its scale-renormalization dynamics that is lost by evaluating only at \(z=1\).

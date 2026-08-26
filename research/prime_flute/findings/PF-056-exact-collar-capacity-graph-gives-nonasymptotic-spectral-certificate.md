# PF-056 — exact collar capacities give a non-asymptotic prime-gap spectral certificate

**Status:** `EXACT-DERIVED` + `POSITIVE-CANDIDATE`; the collar-capacity and Rayleigh–Ritz ingredients are classical, but the exact prime-gap specialization and its use as a finite certificate for essential spectrum appear not to be in the literature checked.

## 1. Motivation

PF-047/PF-054 identify the small spectrum of a strongly pinched prime-derived tangent with the weighted dual path whose edge weights are the short separating geodesic lengths. That statement is asymptotic: it uses the degeneration regime \(L_k\to0\).

There is a more intrinsic finite-scale object already forced by the hyperbolic geometry: the **harmonic capacity of the canonical maximal collar** around each separating geodesic. It gives the exact Dirichlet conductance of the neck, not merely its first small-length term.

This yields a canonical generalized graph Laplacian whose eigenvalues give rigorous upper bounds for the Laplace min–max values of the finite tangent. For a recurrent isolated prime pattern, any bound below \(1/4\) therefore certifies an actual point of the essential spectrum of the infinite prime flute.

No zeta, generating function, or phenomenological graph weight is introduced.

---

## 2. Exact collar conductance

Let \(\gamma\) be a simple closed geodesic of length \(L>0\). Its standard embedded collar has Fermi coordinates

\[
C_L=(-w(L),w(L))\times\mathbb R/\mathbb Z,
\qquad
 ds^2=dr^2+L^2\cosh^2 r\,d\theta^2,
\]

with

\[
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)}.
\]

For functions depending only on \(r\), the harmonic equation is

\[
\frac{d}{dr}\bigl(L\cosh r\,u'(r)\bigr)=0.
\]

Let \(u(-w)=0\), \(u(w)=1\). The minimum Dirichlet energy is the condenser capacity

\[
\kappa(L)=\operatorname{Cap}(C_L)
=\frac{L}{\displaystyle\int_{-w(L)}^{w(L)}\operatorname{sech}r\,dr}.
\]

Using

\[
\int\operatorname{sech}r\,dr=\arctan(\sinh r)
\]

and \(\sinh w(L)=1/\sinh(L/2)\), this becomes exactly

\[
\boxed{
\kappa(L)
=
\frac{L}{\pi-2\arctan(\sinh(L/2))}
=
\frac{L}{4\arctan(e^{-L/2})}.
}
\]

For \(L\to0\),

\[
\boxed{
\kappa(L)=\frac{L}{\pi}+\frac{L^2}{\pi^2}+O(L^3).
}
\]

Thus Burger's use of the geodesic length as a graph edge weight is the first term of an exact harmonic conductance.

The full collar area is

\[
2L\sinh w(L)=\frac{2L}{\sinh(L/2)},
\]

so each half-collar has exact area

\[
\boxed{
a(L)=\frac{L}{\sinh(L/2)}<2.
}
\]

---

## 3. Exact prime-gap substitution

For a prime-derived tangent

\[
H=\{\eta_1<\cdots<\eta_r\},
\qquad
d_i=\eta_{i+1}-\eta_i,
\]

PF-047 gives the nested separating curves

\[
\boxed{
\sinh^2\frac{L_k}{4}
=R_k
:=\frac{d_1+\cdots+d_{k-1}}{d_k},
\qquad k=2,\ldots,r-1.
}
\]

Hence

\[
L_k=4\operatorname{arsinh}\sqrt{R_k}.
\]

Substituting this in the exact collar capacity gives

\[
\boxed{
\kappa_k
:=\kappa(L_k)
=
\frac{\operatorname{arsinh}\sqrt{R_k}}
{\arctan\!\left((\sqrt{1+R_k}-\sqrt{R_k})^2\right)}.
}
\]

The half-collar area becomes

\[
\boxed{
a_k
:=a(L_k)
=
\frac{2\operatorname{arsinh}\sqrt{R_k}}
{\sqrt{R_k}\sqrt{1+R_k}}.
}
\]

These are exact functions of the multi-gap ratios. No pinching limit is used.

In terms of the distinguished cuffs of an occurrence near prime scale \(P\),

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

so

\[
\boxed{
R_k
=
\lim_{P\to\infty}
\sum_{i<k}
\exp\!\left[-\frac{\ell_i(P)-\ell_k(P)}2\right].
}
\]

Therefore the exact neck conductances depend only on the contrasts of the distinguished cuffs after their common radial divergence cancels.

In the hierarchical regime,

\[
R_k\to0,
\qquad
\kappa_k
\sim\frac4\pi\sqrt{R_k}
\sim\frac4\pi\exp\!\left[-\frac{\ell_{k-1}-\ell_k}{4}\right].
\]

---

## 4. Canonical finite-dimensional Dirichlet form

The curves \(L_2,\ldots,L_{r-1}\) form a pants decomposition of

\[
Y_H\cong S_{0,r+1}.
\]

There are

\[
N=r-1
\]

pairs of pants arranged in a path. Every pair of pants has area exactly \(2\pi\).

Remove the standard half-collars of the incident separating curves from each pair of pants. The remaining core of vertex \(i\) has exact area

\[
\boxed{
 m_i
 =2\pi-\sum_{e\sim i} a(L_e).
}
\]

Since a path vertex has degree at most two and \(a(L)<2\),

\[
 m_i>2\pi-4>0.
\]

Let \(c_i\) be a constant assigned to the \(i\)-th core. Extend these constants across each intervening collar by the unique harmonic function with the prescribed boundary values. This defines an \(N\)-dimensional canonical trial space \(\mathcal V_H\subset H^1(Y_H)\).

Its Dirichlet energy is **exactly**

\[
\boxed{
\mathcal E(c)
=
\sum_{e=(i,i+1)}
\kappa(L_e)|c_{i+1}-c_i|^2.
}
\]

Thus, if \(K_H\) is the weighted path Laplacian with conductances \(\kappa(L_e)\),

\[
\mathcal E(c)=c^*K_Hc.
\]

The \(L^2\)-norm also contains a positive contribution from the collars, so in particular

\[
\|u_c\|_{L^2(Y_H)}^2
\ge
c^*M_Hc,
\qquad
M_H=\operatorname{diag}(m_1,\ldots,m_N).
\]

Let

\[
0=\nu_0(H)<\nu_1(H)\le\cdots\le\nu_{N-1}(H)
\]

be the generalized eigenvalues of

\[
K_Hv=\nu M_Hv.
\]

Rayleigh–Ritz/min–max gives the non-asymptotic inequalities

\[
\boxed{
\lambda_j^{\rm mm}(Y_H)\le\nu_j(H),
\qquad j=0,\ldots,N-1,
}
\]

where \(\lambda_j^{\rm mm}\) denotes the Laplace min–max value. In particular,

\[
\boxed{
\nu_j(H)<\frac14
\quad\Longrightarrow\quad
Y_H\text{ has at least }j\text{ positive }L^2\text{ eigenvalues below }\frac14.
}
\]

This is a finite, explicit certificate computed only from the exact prime-gap ratios \(R_k\).

---

## 5. Consequence for the infinite prime flute

Suppose \(H\) is one of the recurrent isolated prime patterns for which PF-034 gives the pointed tangent \(Y_H\). Every \(L^2\) eigenvalue of \(Y_H\) in \((0,1/4)\) produces a Weyl sequence escaping through recurrent copies of the tangent, hence belongs to

\[
\sigma_{\rm ess}(\Delta_{X_{\rm prime}}).
\]

Therefore the capacity matrix gives a direct non-asymptotic implication:

\[
\boxed{
\nu_j(H)<\frac14
\Longrightarrow
\exists\,\lambda_j\in
\sigma_{\rm ess}(\Delta_{X_{\rm prime}})\cap(0,1/4)
\text{ with }\lambda_j\le\nu_j(H).
}
\]

Unlike PF-047/PF-054, this statement does not require \(L_k\to0\) after the tangent has been fixed.

It is an actual finite-pattern spectral certificate.

---

## 6. Recovery of the Burger constant

For short necks,

\[
\kappa(L)=\frac{L}{\pi}+O(L^2).
\]

The vertex mass of a complete limiting pair of pants is \(2\pi\). Consequently the leading effective operator has conductance-to-mass scale

\[
\frac{L/\pi}{2\pi}
=
\boxed{\frac{L}{2\pi^2}},
\]

which is exactly the normalization appearing in Burger's small-eigenvalue theorem.

Thus the factor \(1/(2\pi^2)\) has a direct electrical interpretation:

\[
\boxed{
\text{hyperbolic collar capacity}
\big/\text{pair-of-pants area}.
}
\]

PF-047 is therefore the tropical/small-neck limit of this exact capacity network.

---

## 7. Serious novelty check

Known ingredients, not claimed as new:

1. the standard hyperbolic collar and its conformal cylinder coordinates;
2. condenser capacity as minimum Dirichlet energy and the exact capacity of a cylinder;
3. Rayleigh–Ritz/min–max;
4. Burger's degeneration of small Laplace eigenvalues to a weighted graph;
5. use of capacities in the analysis of degenerating Riemann surfaces.

Directed searches for combinations of `hyperbolic collar capacity`, `capacity matrix`, `weighted graph`, and `small eigenvalues` found substantial classical work on capacities of collars and on graph limits, but no source giving this particular exact finite-dimensional matrix for a chain of cusped pants, nor the prime-gap substitution and essential-spectrum certificate above.

This should therefore be treated conservatively as a **prime-specific exact refinement of classical degeneration theory**, not as a new general theorem about hyperbolic surfaces.

---

## 8. Research consequences and limits

This does **not** say that the full low spectrum of \(Y_H\) equals the spectrum of the capacity graph. The collar conductances give exact energies for the chosen harmonic trial space, while the full surface has additional degrees of freedom and the collars themselves contribute \(L^2\) mass. Equality would be false in general.

What is rigorous is:

- exact edge conductances from the hyperbolic necks;
- exact prime-gap dependence of those conductances;
- a canonical trial space;
- explicit generalized-graph upper bounds on the true Laplace min–max values;
- a below-\(1/4\) criterion that implants genuine spectral points in the essential spectrum of the infinite prime flute when the pattern recurs.

A next useful step is to include the collar \(L^2\)-mass exactly, producing an explicit non-diagonal mass matrix. That would sharpen the finite-scale Ritz operator while preserving its canonical geometric origin.

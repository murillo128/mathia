# MI-014 — One-cancellation shell energy is an anchor Gram problem, and thin windows diagonalize it exactly

**Evidence level:** proved by VIS-204 and VIS-209--VIS-210 for the autocorrelation-taper one-cancellation shell family. No uniform diagonal-energy decay or theorem outside the stated thin-window cone is claimed.

VIS-208 closes the entire noncancelling determinant band in start-averaged energy under explicit window conditions. VIS-209 then shows that the first surviving layer is not an arbitrary high-multiplicity shell family. With `Psi_(u,t)=b_(log(u/t))` and `G=Psi^2`, every one-cancellation shell is an off-diagonal entry of one PSD Gram kernel, `tr G=R`, and

`E_1 = 4[tr(G^2)-sum_u G_(u,u)^2]`.

That reduction initially makes spectral spreading of the anchor profiles the natural target. VIS-210 shows that even this can be too coarse in the thin-window regime. After the exact six-anchor reduction, if `L_tri>5R-5` then the anchor supports of distinct shell indices are disjoint, so the fluctuation Gram is **exactly diagonal**. In the fringe `L_tri>4R-3`, the only possible cross-shell coupling is the explicit `6/5` resonance `L_tri=5s-6r+1`.

The endpoint therefore changes again. Inside the collision-free cone, there is no cross-shell spectral-spreading problem at all: `||G||_op=max_r G_rr`, and the remaining theorem is a uniform bound or asymptotic for the diagonal shell energies `G_rr=sum_c alpha_r(c)^2`. Near the cone boundary one must add only the explicitly parameterized sparse resonance fringe, not a generic dense covariance estimate.

This gives a useful hierarchy for the one-cancellation layer: first expose the PSD Gram structure; then determine whether support geometry diagonalizes it; only after those exact reductions estimate the surviving diagonal weights or resonance amplitudes. Bounding shell multiplicities or a full generic Gram norm before this support analysis pays for interactions that may be identically absent.

**Boundary.** VIS-210 does not bound the diagonal energies, and outside `L_tri>4R-3` additional anchor families can collide. Neither VIS-209 nor VIS-210 addresses higher-cancellation shells or upgrades start-averaged control to uniform-in-start control.